import os.path as op
from contextlib import nullcontext as does_not_raise

import numpy as np
import pytest
import torch

import plenoptic as po
from conftest import DEVICE


class TestSequences:
    def test_deviation_from_line_and_brownian_bridge(self):
        """this probabilistic test passes with high probability
        in high dimensions, but for reproducibility we
        set the seed manually."""
        torch.manual_seed(0)
        t = 2**6
        d = 2**14
        sqrt_d = int(np.sqrt(d))
        start = torch.randn(1, d).reshape(1, 1, sqrt_d, sqrt_d).to(DEVICE)
        stop = torch.randn(1, d).reshape(1, 1, sqrt_d, sqrt_d).to(DEVICE)
        b = po.tools.sample_brownian_bridge(start, stop, t, d**0.5)
        a, f = po.tools.deviation_from_line(b, normalize=True)
        assert torch.abs(a[t // 2] - 0.5) < 1e-2, f"{a[t // 2]}"
        assert torch.abs(f[t // 2] - 2**0.5 / 2) < 1e-2, f"{f[t // 2]}"

    @pytest.mark.parametrize("normalize", [True, False])
    def test_deviation_from_line_multichannel(self, normalize, einstein_img):
        einstein_img = einstein_img.repeat(1, 3, 1, 1)
        seq = po.tools.translation_sequence(einstein_img)
        dist_along, dist_from = po.tools.deviation_from_line(seq, normalize)
        assert dist_along.shape[0] == seq.shape[0], (
            "Distance along line has wrong number of transitions!"
        )
        assert dist_from.shape[0] == seq.shape[0], (
            "Distance from  line has wrong number of transitions!"
        )

    @pytest.mark.parametrize("n_steps", [1, 10])
    @pytest.mark.parametrize("max_norm", [0, 1, 10])
    @pytest.mark.parametrize("multichannel", [False, True])
    def test_brownian_bridge(
        self, einstein_img, curie_img, n_steps, multichannel, max_norm
    ):
        if multichannel:
            einstein_img = einstein_img.repeat(1, 3, 1, 1)
            curie_img = curie_img.repeat(1, 3, 1, 1)
        bridge = po.tools.sample_brownian_bridge(
            einstein_img, curie_img, n_steps, max_norm
        )
        assert bridge.shape == (
            n_steps + 1,
            *einstein_img.shape[1:],
        ), "sample_brownian_bridge returned a tensor of the wrong shape!"

    @pytest.mark.parametrize("fail", ["batch", "same_shape", "n_steps", "max_norm"])
    def test_brownian_bridge_fail(self, einstein_img, curie_img, fail):
        n_steps = 2
        max_norm = 1
        if fail == "batch":
            einstein_img = einstein_img.repeat(2, 1, 1, 1)
            curie_img = curie_img.repeat(2, 1, 1, 1)
            expectation = pytest.raises(
                ValueError, match="input_tensor batch dimension must be 1"
            )
        elif fail == "same_shape":
            # rand_like preserves DEVICE and dtype
            curie_img = torch.rand_like(curie_img)[..., :128, :128]
            expectation = pytest.raises(
                ValueError, match="start and stop must be same shape"
            )
        elif fail == "n_steps":
            n_steps = 0
            expectation = pytest.raises(ValueError, match="n_steps must be positive")
        elif fail == "max_norm":
            max_norm = -1
            expectation = pytest.raises(
                ValueError, match="max_norm must be non-negative"
            )
        with expectation:
            po.tools.sample_brownian_bridge(einstein_img, curie_img, n_steps, max_norm)

    @pytest.mark.parametrize("n_steps", [1, 10])
    @pytest.mark.parametrize("multichannel", [False, True])
    def test_straight_line(self, einstein_img, curie_img, n_steps, multichannel):
        if multichannel:
            einstein_img = einstein_img.repeat(1, 3, 1, 1)
            curie_img = curie_img.repeat(1, 3, 1, 1)
        line = po.tools.make_straight_line(einstein_img, curie_img, n_steps)
        assert line.shape == (
            n_steps + 1,
            *einstein_img.shape[1:],
        ), "make_straight_line returned a tensor of the wrong shape!"

    @pytest.mark.parametrize("fail", ["batch", "same_shape", "n_steps"])
    def test_straight_line_fail(self, einstein_img, curie_img, fail):
        n_steps = 2
        if fail == "batch":
            einstein_img = einstein_img.repeat(2, 1, 1, 1)
            curie_img = curie_img.repeat(2, 1, 1, 1)
            expectation = pytest.raises(
                ValueError, match="input_tensor batch dimension must be 1"
            )
        elif fail == "same_shape":
            # rand_like preserves DEVICE and dtype
            curie_img = torch.rand_like(curie_img)[..., :128, :128]
            expectation = pytest.raises(
                ValueError, match="start and stop must be same shape"
            )
        elif fail == "n_steps":
            n_steps = 0
            expectation = pytest.raises(ValueError, match="n_steps must be positive")
        with expectation:
            po.tools.make_straight_line(einstein_img, curie_img, n_steps)

    @pytest.mark.parametrize("n_steps", [0, 1, 10])
    @pytest.mark.parametrize("multichannel", [False, True])
    def test_translation_sequence(self, einstein_img, n_steps, multichannel):
        if n_steps == 0:
            expectation = pytest.raises(ValueError, match="n_steps must be positive")
        else:
            expectation = does_not_raise()
        if multichannel:
            einstein_img = einstein_img.repeat(1, 3, 1, 1)
        with expectation:
            shifted = po.tools.translation_sequence(einstein_img, n_steps)
            assert torch.equal(shifted[0], einstein_img[0]), (
                "somehow first frame changed!"
            )
            assert torch.equal(shifted[1, 0, :, 1], shifted[0, 0, :, 0]), (
                "wrong dimension was translated!"
            )

    @pytest.mark.parametrize(
        "func",
        [
            "make_straight_line",
            "translation_sequence",
            "sample_brownian_bridge",
            "deviation_from_line",
        ],
    )
    def test_preserve_device(self, einstein_img, func):
        kwargs = {}
        if func != "deviation_from_line":
            kwargs["n_steps"] = 5
            if func != "translation_sequence":
                kwargs["stop"] = torch.rand_like(einstein_img)
        seq = getattr(po.tools, func)(einstein_img, **kwargs)
        # kinda hacky -- deviation_from_line returns a tuple, all the others
        # return a 4d tensor. regardless seq[0] will be a tensor
        assert seq[0].device == einstein_img.device, f"{func} changed device!"


class TestGeodesic:
    @pytest.mark.parametrize("model", ["frontend.OnOff.nograd"], indirect=True)
    @pytest.mark.parametrize("init", ["straight", "bridge"])
    @pytest.mark.parametrize("optimizer", [None, "SGD"])
    @pytest.mark.parametrize("n_steps", [5, 10])
    def test_texture(self, einstein_img_small, model, init, optimizer, n_steps):
        sequence = po.tools.translation_sequence(einstein_img_small, n_steps)
        moog = po.synth.Geodesic(sequence[:1], sequence[-1:], model, n_steps)
        optimizer = None
        if optimizer == "SGD":
            optimizer = torch.optim.SGD
        moog.setup(init, optimizer=optimizer)
        moog.synthesize(max_iter=5)
        po.synth.geodesic.plot_loss(moog)
        po.synth.geodesic.plot_deviation_from_line(moog, natural_video=sequence)
        moog.calculate_jerkiness()

    @pytest.mark.parametrize("model", ["frontend.OnOff.nograd"], indirect=True)
    def test_endpoints_dont_change(self, einstein_small_seq, model):
        moog = po.synth.Geodesic(
            einstein_small_seq[:1],
            einstein_small_seq[-1:],
            model,
            5,
        )
        moog.synthesize(max_iter=5)
        assert torch.equal(moog.geodesic[0], einstein_small_seq[0]), (
            "Somehow first endpoint changed!"
        )
        assert torch.equal(moog.geodesic[-1], einstein_small_seq[-1]), (
            "Somehow last endpoint changed!"
        )
        assert not torch.equal(moog.pixelfade[1:-1], moog.geodesic[1:-1]), (
            "Somehow middle of geodesic didn't changed!"
        )

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize(
        "fail",
        [
            False,
            "img_a",
            "img_b",
            "model",
            "n_steps",
            "range_penalty",
            "allowed_range",
        ],
    )
    @pytest.mark.parametrize("range_penalty", [0.1, 0])
    @pytest.mark.parametrize("allowed_range", [(0, 1), (-1, 1)])
    def test_save_load(
        self, einstein_small_seq, model, fail, range_penalty, allowed_range, tmp_path
    ):
        img_a = einstein_small_seq[:1]
        img_b = einstein_small_seq[-1:]
        n_steps = 3
        moog = po.synth.Geodesic(
            img_a,
            img_b,
            model,
            n_steps,
            range_penalty_lambda=range_penalty,
            allowed_range=allowed_range,
        )
        moog.synthesize(max_iter=4)
        moog.save(op.join(tmp_path, "test_geodesic_save_load.pt"))
        if fail:
            if fail == "img_a":
                img_a = torch.rand_like(img_a)
                expectation = pytest.raises(
                    ValueError,
                    match=(
                        "Saved and initialized attribute image_a have different values"
                    ),
                )
            elif fail == "img_b":
                img_b = torch.rand_like(img_b)
                expectation = pytest.raises(
                    ValueError,
                    match=(
                        "Saved and initialized attribute image_b have different values"
                    ),
                )
            elif fail == "model":
                model = po.simul.Gaussian(30).to(DEVICE)
                po.tools.remove_grad(model)
                expectation = pytest.raises(
                    ValueError,
                    match="Saved and initialized model output have different values",
                )
            elif fail == "n_steps":
                n_steps = 5
                expectation = pytest.raises(
                    ValueError,
                    match="Saved and initialized n_steps are different",
                )
            elif fail == "allowed_range":
                allowed_range = (0, 5)
                expectation = pytest.raises(
                    ValueError,
                    match=("Saved and initialized allowed_range are different"),
                )
            elif fail == "range_penalty":
                range_penalty = 0.5
                expectation = pytest.raises(
                    ValueError,
                    match=("Saved and initialized range_penalty_lambda are different"),
                )
            moog_copy = po.synth.Geodesic(
                img_a,
                img_b,
                model,
                n_steps,
                range_penalty_lambda=range_penalty,
                allowed_range=allowed_range,
            )
            with expectation:
                moog_copy.load(
                    op.join(tmp_path, "test_geodesic_save_load.pt"),
                    map_location=DEVICE,
                )
        else:
            moog_copy = po.synth.Geodesic(
                img_a,
                img_b,
                model,
                n_steps,
                range_penalty_lambda=range_penalty,
                allowed_range=allowed_range,
            )
            moog_copy.load(
                op.join(tmp_path, "test_geodesic_save_load.pt"),
                map_location=DEVICE,
            )
            for k in ["image_a", "image_b", "pixelfade", "geodesic"]:
                if not getattr(moog, k).allclose(getattr(moog_copy, k), rtol=1e-2):
                    raise ValueError(
                        "Something went wrong with saving and loading!"
                        f" {k} not the same"
                    )
            # check that can resume
            moog_copy.synthesize(max_iter=4)

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize("seq", ["straight", "bridge", "FAIL"])
    def test_setup_initial_seq(self, einstein_img, model, seq):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        if seq == "FAIL":
            expectation = pytest.raises(
                ValueError, match="Don't know how to handle initial_"
            )
        else:
            expectation = does_not_raise()
        with expectation:
            geod.setup(seq)
            geod.synthesize(5)

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    def test_setup_fail(self, einstein_img, model):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.setup()
        with pytest.raises(ValueError, match="setup\(\) can only be called once"):
            geod.setup()

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    def test_synth_then_setup(self, einstein_img, model, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.setup(optimizer=torch.optim.SGD)
        geod.synthesize(max_iter=4)
        geod.save(op.join(tmp_path, "test_geodesic_synth_then_setup.pt"))
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.load(op.join(tmp_path, "test_geodesic_synth_then_setup.pt"))
        with pytest.raises(ValueError, match="Don't know how to initialize"):
            geod.synthesize(5)
        geod.setup(optimizer=torch.optim.SGD)
        geod.synthesize(5)

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    def test_setup_load_fail(self, einstein_img, model, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(max_iter=4)
        geod.save(op.join(tmp_path, "test_geodesic_setup_load_fail.pt"))
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.load(op.join(tmp_path, "test_geodesic_setup_load_fail.pt"))
        with pytest.raises(
            ValueError, match="Cannot set initial_sequence after calling load"
        ):
            geod.setup(po.data.curie())

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    def test_load_pixelfade(self, einstein_img, model, tmp_path):
        # the only way this can change, really, is if I change the make_straight_line
        # function, but might as well make sure
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(max_iter=4, store_progress=True)
        geod.save(op.join(tmp_path, "test_geodesic_load_pixelfade.pt"))
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.pixelfade = torch.rand_like(geod.pixelfade)
        with pytest.raises(
            ValueError,
            match=("Saved and initialized attribute pixelfade have different values"),
        ):
            geod.load(op.join(tmp_path, "test_geodesic_load_pixelfade.pt"))

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    def test_load_init_fail(self, einstein_img, model, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(max_iter=4, store_progress=True)
        geod.save(op.join(tmp_path, "test_geodesic_load_init_fail.pt"))
        with pytest.raises(
            ValueError, match="load can only be called with a just-initialized"
        ):
            geod.load(op.join(tmp_path, "test_geodesic_load_init_fail.pt"))

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    def test_examine_saved_object(self, einstein_img, model, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(max_iter=4, store_progress=True)
        geod.save(op.join(tmp_path, "test_geodesic_examine .pt"))
        po.tools.examine_saved_synthesis(op.join(tmp_path, "test_geodesic_examine .pt"))

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize("synth_type", ["eig", "mad"])
    def test_load_object_type(self, einstein_img, model, synth_type, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(max_iter=4, store_progress=True)
        geod.save(op.join(tmp_path, "test_geodesic_load_object_type.pt"))
        if synth_type == "eig":
            geod = po.synth.Eigendistortion(einstein_img, model)
        elif synth_type == "mad":
            geod = po.synth.MADCompetition(
                einstein_img, po.metric.mse, po.metric.mse, "min"
            )
        with pytest.raises(
            ValueError, match="Saved object was a.* but initialized object is"
        ):
            geod.load(op.join(tmp_path, "test_geodesic_load_object_type.pt"))

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize("model_behav", ["dtype", "shape", "name"])
    def test_load_model_change(self, einstein_img, model, model_behav, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(max_iter=4, store_progress=True)
        geod.save(op.join(tmp_path, "test_geodesic_load_model_change.pt"))
        if model_behav == "dtype":
            # this actually gets raised in the model validation step (during init), not
            # load.
            expectation = pytest.raises(TypeError, match="model changes precision")
        elif model_behav == "shape":
            expectation = pytest.raises(
                ValueError,
                match="Saved and initialized model output have different shape",
            )
        elif model_behav == "name":
            expectation = pytest.raises(
                ValueError, match="Saved and initialized model have different names"
            )

        class NewModel(torch.nn.Module):
            def __init__(self):
                super().__init__()
                self.model = model

            def forward(self, x):
                if model_behav == "dtype":
                    return self.model(x).to(torch.float64)
                elif model_behav == "shape":
                    return self.model(x).flatten(-2)
                elif model_behav == "name":
                    return self.model(x)

        with expectation:
            geod = po.synth.Geodesic(einstein_img, einstein_img / 2, NewModel())
            geod.load(op.join(tmp_path, "test_geodesic_load_model_change.pt"))

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize("attribute", ["saved", "init"])
    def test_load_attributes(self, einstein_img, model, attribute, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(max_iter=4, store_progress=True)
        if attribute == "saved":
            geod.test = "BAD"
            err_str = "Saved"
        geod.save(op.join(tmp_path, "test_geodesic_load_attributes.pt"))
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        if attribute == "init":
            geod.test = "BAD"
            err_str = "Initialized"
        with pytest.raises(
            ValueError, match=f"{err_str} object has 1 attribute\(s\) not present"
        ):
            geod.load(op.join(tmp_path, "test_geodesic_load_attributes.pt"))

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize(
        "optim_opts", [None, "SGD", "SGD-args", "Adam", "Adam-args"]
    )
    @pytest.mark.parametrize("fail", [True, False])
    def test_load_optimizer(self, curie_img, model, optim_opts, fail, tmp_path):
        geod = po.synth.Geodesic(curie_img, curie_img / 2, model)
        optimizer = None
        optimizer_kwargs = None
        check_optimizer = [torch.optim.Adam, {"eps": 1e-8, "lr": 0.001}]
        if optim_opts is not None:
            if "Adam" in optim_opts:
                optimizer = torch.optim.Adam
            elif "SGD" in optim_opts:
                optimizer = torch.optim.SGD
                check_optimizer[0] = torch.optim.SGD
                check_optimizer[1] = {"lr": 0.001}
            if "args" in optim_opts:
                optimizer_kwargs = {"lr": 1}
                check_optimizer[1] = {"lr": 1}
        geod.setup(optimizer=optimizer, optimizer_kwargs=optimizer_kwargs)
        geod.synthesize(max_iter=5)
        geod.save(op.join(tmp_path, "test_geodesic_optimizer.pt"))
        geod = po.synth.Geodesic(curie_img, curie_img / 2, model)
        geod.load(op.join(tmp_path, "test_geodesic_optimizer.pt"))
        optimizer_kwargs = None
        if not fail:
            if optim_opts is not None:
                if "Adam" in optim_opts:
                    optimizer = torch.optim.Adam
                elif "SGD" in optim_opts:
                    optimizer = torch.optim.SGD
            expectation = does_not_raise()
        else:
            expect_str = "User-specified optimizer must have same type"
            if optim_opts is None:
                optimizer = torch.optim.SGD
            else:
                if optim_opts == "Adam":
                    optimizer = torch.optim.SGD
                elif optim_opts == "Adam-args":
                    optimizer = torch.optim.Adam
                    optimizer_kwargs = {"lr": 1}
                    expect_str = (
                        "When initializing optimizer after load, optimizer_kwargs"
                    )
                elif optim_opts == "SGD":
                    optimizer = None
                    expect_str = "Don't know how to initialize saved optimizer"
                elif optim_opts == "SGD-args":
                    optimizer = torch.optim.SGD
                    optimizer_kwargs = {"lr": 1}
                    expect_str = (
                        "When initializing optimizer after load, optimizer_kwargs"
                    )
            expectation = pytest.raises(ValueError, match=expect_str)
        with expectation:
            geod.setup(optimizer=optimizer, optimizer_kwargs=optimizer_kwargs)
            geod.synthesize(max_iter=5)
            if not isinstance(geod.optimizer, check_optimizer[0]):
                raise ValueError("Didn't properly set optimizer!")
            state_dict = geod.optimizer.state_dict()["param_groups"][0]
            for k, v in check_optimizer[1].items():
                if state_dict[k] != v:
                    raise ValueError(
                        "Didn't properly set optimizer kwargs! "
                        f"Expected {v} but got {state_dict[k]}!"
                    )

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize("load", [True, False])
    def test_resume_synthesis(self, einstein_img, model, load, tmp_path):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        # Adam has some stochasticity in its initialization(?), so this test doesn't
        # quite work with it (it does if you do po.tools.set_seed(2) at the top of the
        # function)
        geod.setup(optimizer=torch.optim.SGD)
        geod.synthesize(10)
        geod_copy = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod_copy.setup(optimizer=torch.optim.SGD)
        geod_copy.synthesize(5)
        if load:
            geod_copy.save(op.join(tmp_path, "test_geodesic_resume_synthesis.pt"))
            geod_copy = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
            geod_copy.load(op.join(tmp_path, "test_geodesic_resume_synthesis.pt"))
            geod_copy.setup(optimizer=torch.optim.SGD)
            geod_copy.synthesize(5)
        else:
            geod_copy.synthesize(5)
        if not torch.allclose(geod.geodesic, geod_copy.geodesic):
            raise ValueError("Resuming synthesis different than just continuing!")

    # test that we support models with 3d and 4d outputs
    @pytest.mark.parametrize(
        "model",
        ["PortillaSimoncelli", "frontend.LinearNonlinear.nograd"],
        indirect=True,
    )
    def test_model_dimensionality(self, einstein_img, model):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        geod.synthesize(5)

    @pytest.mark.parametrize(
        "model", ["frontend.LinearNonlinear.nograd"], indirect=True
    )
    @pytest.mark.parametrize(
        "optimizer", ["SGD", "SGD-args", "Adam", "Adam-args", None]
    )
    def test_optimizer(self, einstein_img, model, optimizer):
        geod = po.synth.Geodesic(einstein_img, einstein_img / 2, model)
        optimizer = None
        optimizer_kwargs = None
        check_optimizer = [torch.optim.Adam, {"eps": 1e-8, "lr": 0.001}]
        if optimizer == "Adam":
            optimizer = torch.optim.Adam
        elif optimizer == "Adam-args":
            optimizer = torch.optim.Adam
            optimizer_kwargs = {"eps": 1e-5}
            check_optimizer[1]["eps"] = 1e-5
        elif optimizer == "SGD":
            optimizer = torch.optim.SGD
            check_optimizer = [torch.optim.SGD, {"lr": 0.001}]
        elif optimizer == "SGD-args":
            optimizer = torch.optim.SGD
            optimizer_kwargs = {"lr": 1}
            check_optimizer = [torch.optim.SGD, {"lr": 1}]
        geod.setup(
            optimizer=optimizer,
            optimizer_kwargs=optimizer_kwargs,
        )
        geod.synthesize(max_iter=5)
        if not isinstance(geod.optimizer, check_optimizer[0]):
            raise ValueError("Didn't properly set optimizer!")
        state_dict = geod.optimizer.state_dict()["param_groups"][0]
        for k, v in check_optimizer[1].items():
            if state_dict[k] != v:
                raise ValueError(
                    "Didn't properly set optimizer kwargs! "
                    f"Expected {v} but got {state_dict[k]}!"
                )

    @pytest.mark.skipif(DEVICE.type == "cpu", reason="Only makes sense to test on cuda")
    @pytest.mark.parametrize("model", ["Identity"], indirect=True)
    def test_map_location(self, einstein_small_seq, model, tmp_path):
        moog = po.synth.Geodesic(einstein_small_seq[:1], einstein_small_seq[-1:], model)
        moog.synthesize(max_iter=4, store_progress=True)
        moog.save(op.join(tmp_path, "test_geodesic_map_location.pt"))
        # calling load with map_location effectively switches everything
        # over to that device
        model.to("cpu")
        moog_copy = po.synth.Geodesic(
            einstein_small_seq[:1].to("cpu"), einstein_small_seq[-1:].to("cpu"), model
        )
        moog_copy.load(
            op.join(tmp_path, "test_geodesic_map_location.pt"),
            map_location="cpu",
        )
        assert moog_copy.geodesic.device.type == "cpu"
        assert moog_copy.image_a.device.type == "cpu"
        moog_copy.synthesize(max_iter=4, store_progress=True)
        # reset model device for other tests
        model.to(DEVICE)

    @pytest.mark.parametrize("model", ["Identity"], indirect=True)
    @pytest.mark.parametrize("to_type", ["dtype", "device"])
    def test_to(self, einstein_small_seq, model, to_type):
        moog = po.synth.Geodesic(einstein_small_seq[:1], einstein_small_seq[-1:], model)
        moog.synthesize(max_iter=5)
        if to_type == "dtype":
            moog.to(torch.float16)
            assert moog.image_a.dtype == torch.float16
            assert moog.geodesic.dtype == torch.float16
        # can only run this one if we're on a device with CPU and GPU.
        elif to_type == "device" and DEVICE.type != "cpu":
            moog.to("cpu")
        moog.geodesic - moog.image_a

    @pytest.mark.parametrize("model", ["Identity"], indirect=True)
    def test_change_precision_save_load(self, einstein_small_seq, model, tmp_path):
        # Identity model doesn't change when you call .to() with a dtype
        # (unlike those models that have weights) so we use it here
        moog = po.synth.Geodesic(einstein_small_seq[:1], einstein_small_seq[-1:], model)
        moog.synthesize(max_iter=5)
        moog.to(torch.float64)
        assert moog.geodesic.dtype == torch.float64, "dtype incorrect!"
        moog.save(op.join(tmp_path, "test_change_prec_save_load.pt"))
        seq = einstein_small_seq.to(torch.float64)
        moog_copy = po.synth.Geodesic(seq[:1], seq[-1:], model)
        moog_copy.load(op.join(tmp_path, "test_change_prec_save_load.pt"))
        moog_copy.synthesize(max_iter=5)
        assert moog_copy.geodesic.dtype == torch.float64, "dtype incorrect!"

    # this determines whether we mix across channels or treat them separately,
    # both of which are supported
    @pytest.mark.parametrize("model", ["ColorModel", "Identity"], indirect=True)
    def test_multichannel(self, color_img, model):
        img = color_img[..., :64, :64]
        seq = po.tools.translation_sequence(img, 5)
        moog = po.synth.Geodesic(seq[:1], seq[-1:], model, 5)
        moog.synthesize(max_iter=5)
        assert moog.geodesic.shape[1:] == img.shape[1:], (
            "Geodesic image should have same number of channels, height, width"
            " shape as input!"
        )

    @pytest.mark.parametrize("model", ["frontend.OnOff.nograd"], indirect=True)
    @pytest.mark.parametrize("func", ["objective_function", "calculate_jerkiness"])
    def test_funcs_external_tensor(self, einstein_small_seq, model, func):
        moog = po.synth.Geodesic(
            einstein_small_seq[:1], einstein_small_seq[-1:], model, 5
        )
        moog.setup()
        no_arg = getattr(moog, func)()
        arg_tensor = torch.rand_like(moog.geodesic)
        # calculate jerkiness requires tensor to have gradient attached
        # (because we use autodiff functions)
        if func == "calculate_jerkiness":
            arg_tensor.requires_grad_()
        with_arg = getattr(moog, func)(arg_tensor)
        assert not torch.equal(no_arg, with_arg), (
            f"{func} is not using the input tensor!"
        )

    @pytest.mark.parametrize("model", ["frontend.OnOff.nograd"], indirect=True)
    def test_continue(self, einstein_small_seq, model):
        moog = po.synth.Geodesic(
            einstein_small_seq[:1], einstein_small_seq[-1:], model, 5
        )
        moog.synthesize(max_iter=3, store_progress=True)
        moog.synthesize(max_iter=3, store_progress=True)

    @pytest.mark.parametrize("model", ["frontend.OnOff.nograd"], indirect=True)
    def test_nan_loss(self, model, einstein_small_seq):
        # clone to prevent NaN from showing up in other tests
        seq = einstein_small_seq.clone()
        moog = po.synth.Geodesic(seq[:1], seq[-1:], model, 5)
        moog.synthesize(max_iter=5)
        moog.image_a[..., 0, 0] = torch.nan
        with pytest.raises(ValueError, match="Found a NaN in loss during optimization"):
            moog.synthesize(max_iter=1)

    @pytest.mark.parametrize("model", ["frontend.OnOff.nograd"], indirect=True)
    @pytest.mark.parametrize("store_progress", [True, 2, 3])
    def test_store_progress(self, einstein_small_seq, model, store_progress):
        moog = po.synth.Geodesic(
            einstein_small_seq[:1], einstein_small_seq[-1:], model, 5
        )
        max_iter = 3
        if store_progress == 3:
            max_iter = 6
        moog.synthesize(max_iter=max_iter, store_progress=store_progress)
        assert len(moog.step_energy) == np.ceil(max_iter / store_progress), (
            "Didn't end up with enough step_energy after first synth!"
        )
        assert len(moog.dev_from_line) == np.ceil(max_iter / store_progress), (
            "Didn't end up with enough dev_from_line after first synth!"
        )
        assert len(moog.losses) == max_iter, (
            "Didn't end up with enough losses after first synth!"
        )
        moog.synthesize(max_iter=max_iter, store_progress=store_progress)
        assert len(moog.step_energy) == np.ceil(2 * max_iter / store_progress), (
            "Didn't end up with enough step_energy after second synth!"
        )
        assert len(moog.dev_from_line) == np.ceil(2 * max_iter / store_progress), (
            "Didn't end up with enough dev_from_line after second synth!"
        )
        assert len(moog.losses) == 2 * max_iter, (
            "Didn't end up with enough losses after second synth!"
        )

    @pytest.mark.parametrize("model", ["frontend.OnOff.nograd"], indirect=True)
    def test_stop_criterion(self, einstein_small_seq, model):
        # checking that this hits the criterion and stops early, so set seed
        # for reproducibility
        po.tools.set_seed(0)
        moog = po.synth.Geodesic(
            einstein_small_seq[:1], einstein_small_seq[-1:], model, 5
        )
        moog.synthesize(max_iter=10, stop_criterion=0.06, stop_iters_to_check=1)
        assert (abs(moog.pixel_change_norm[-1:]) < 0.06).all(), (
            "Didn't stop when hit criterion!"
        )
        assert (abs(moog.pixel_change_norm[:-1]) > 0.06).all(), (
            "Stopped after hit criterion!"
        )
