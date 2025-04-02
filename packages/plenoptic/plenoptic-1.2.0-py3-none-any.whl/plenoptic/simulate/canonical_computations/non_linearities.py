import torch

from ...tools.conv import blur_downsample, upsample_blur
from ...tools.signal import polar_to_rectangular, rectangular_to_polar


def rectangular_to_polar_dict(coeff_dict, residuals=False):
    """Return the complex modulus and the phase of each complex tensor in a dictionary.

    Parameters
    ----------
    coeff_dict : dict
       A dictionary containing complex tensors.
    dim : int, optional
       The dimension that contains the real and imaginary components.
    residuals: bool, optional
        An option to carry around residuals in the energy branch.
    Returns
    -------
    energy : dict
        The dictionary of torch.Tensors containing the local complex
        modulus of ``coeff_dict``.
    state: dict
        The dictionary of torch.Tensors containing the local phase of
        ``coeff_dict``.

    """
    energy = {}
    state = {}
    for key in coeff_dict:
        # ignore residuals
        if isinstance(key, tuple) or not key.startswith("residual"):
            energy[key], state[key] = rectangular_to_polar(coeff_dict[key])

    if residuals:
        energy["residual_lowpass"] = coeff_dict["residual_lowpass"]
        energy["residual_highpass"] = coeff_dict["residual_highpass"]

    return energy, state


def polar_to_rectangular_dict(energy, state, residuals=True):
    """Return the real and imaginary parts of tensor in a dictionary.

    Parameters
    ----------
    energy : dict
        The dictionary of torch.Tensors containing the local complex
        modulus.
    state : dict
        The dictionary of torch.Tensors containing the local phase.
    dim : int, optional
       The dimension that contains the real and imaginary components.
    residuals: bool, optional
        An option to carry around residuals in the energy branch.

    Returns
    -------
    coeff_dict : dict
       A dictionary containing complex tensors of coefficients.
    """

    coeff_dict = {}
    for key in energy:
        # ignore residuals

        if isinstance(key, tuple) or not key.startswith("residual"):
            coeff_dict[key] = polar_to_rectangular(energy[key], state[key])

    if residuals:
        coeff_dict["residual_lowpass"] = energy["residual_lowpass"]
        coeff_dict["residual_highpass"] = energy["residual_highpass"]

    return coeff_dict


def local_gain_control(x, epsilon=1e-8):
    """Spatially local gain control.

    Parameters
    ----------
    x : torch.Tensor
        Tensor of shape (batch, channel, height, width)
    epsilon: float, optional
        Small constant to avoid division by zero.

    Returns
    -------
    norm : torch.Tensor
        The local energy of ``x``. Note that it is down sampled by a
        factor 2 in (unlike rect2pol).
    direction: torch.Tensor
        The local phase of ``x`` (aka. local unit vector, or local
        state)

    Notes
    -----
    This function is an analogue to rectangular_to_polar for
    real valued signals.

    Norm and direction (analogous to complex modulus and phase) are
    defined using blurring operator and division.  Indeed blurring the
    responses removes high frequencies introduced by the squaring
    operation. In the complex case adding the quadrature pair response
    has the same effect (note that this is most clearly seen in the
    frequency domain).  Here computing the direction (phase) reduces to
    dividing out the norm (modulus), indeed the signal only has one real
    component. This is a normalization operation (local unit vector),
    hence the connection to local gain control.
    """

    # these could be parameters, but no use case so far
    p = 2.0

    norm = blur_downsample(torch.abs(x**p)).pow(1 / p)
    odd = torch.as_tensor(x.shape)[2:4] % 2
    direction = x / (upsample_blur(norm, odd) + epsilon)

    return norm, direction


def local_gain_release(norm, direction, epsilon=1e-8):
    """Spatially local gain release.

    Parameters
    ----------
    norm : torch.Tensor
        The local energy of ``x``. Note that it is down sampled by a
        factor 2 in (unlike rect2pol).
    direction: torch.Tensor
        The local phase of ``x`` (aka. local unit vector, or local
        state)
    epsilon: float, optional
        Small constant to avoid division by zero.
    Returns
    -------
    x : torch.Tensor
        Tensor of shape (batch, channel, height, width)

    Notes
    -----
    This function is an analogue to polar_to_rectangular for
    real valued signals.

    Norm and direction (analogous to complex modulus and phase) are
    defined using blurring operator and division.  Indeed blurring the
    responses removes high frequencies introduced by the squaring
    operation. In the complex case adding the quadrature pair response
    has the same effect (note that this is most clearly seen in the
    frequency domain).  Here computing the direction (phase) reduces to
    dividing out the norm (modulus), indeed the signal only has one real
    component. This is a normalization operation (local unit vector),
    hence the connection to local gain control.
    """

    odd = torch.as_tensor(direction.shape)[2:4] % 2
    x = direction * (upsample_blur(norm, odd) + epsilon)
    return x


def local_gain_control_dict(coeff_dict, residuals=True):
    """Spatially local gain control, for each element in a dictionary.

    Parameters
    ----------
    coeff_dict : dict
        A dictionary containing tensors of shape (batch, channel, height, width)
    residuals: bool, optional
        An option to carry around residuals in the energy dict.
        Note that the transformation is not applied to the residuals,
        that is dictionary elements with a key starting in "residual".

    Returns
    -------
    energy : dict
        The dictionary of torch.Tensors containing the local energy of
        ``x``.
    state: dict
        The dictionary of torch.Tensors containing the local phase of
        ``x``.

    Notes
    -----
    Note that energy and state is not computed on the residuals.

    The inverse operation is achieved by `local_gain_release_dict`.
    This function is an analogue to rectangular_to_polar_dict for real
    valued signals. For more details, see :meth:`local_gain_control`
    """
    energy = {}
    state = {}

    for key in coeff_dict:
        if isinstance(key, tuple) or not key.startswith("residual"):
            energy[key], state[key] = local_gain_control(coeff_dict[key])

    if residuals:
        energy["residual_lowpass"] = coeff_dict["residual_lowpass"]
        energy["residual_highpass"] = coeff_dict["residual_highpass"]

    return energy, state


def local_gain_release_dict(energy, state, residuals=True):
    """Spatially local gain release, for each element in a dictionary.

    Parameters
    ----------
    energy : dict
        The dictionary of torch.Tensors containing the local energy of
        ``x``.
    state: dict
        The dictionary of torch.Tensors containing the local phase of
        ``x``.
    residuals: bool, optional
        An option to carry around residuals in the energy dict.
        Note that the transformation is not applied to the residuals,
        that is dictionary elements with a key starting in "residual".

    Returns
    -------
    coeff_dict : dict
        A dictionary containing tensors of shape (batch, channel, height, width)

    Notes
    -----
    The inverse operation to `local_gain_control_dict`.
    This function is  an analogue to polar_to_rectangular_dict for real
    valued signals. For more details, see :meth:`local_gain_release`
    """
    coeff_dict = {}

    for key in energy:
        if isinstance(key, tuple) or not key.startswith("residual"):
            coeff_dict[key] = local_gain_release(energy[key], state[key])

    if residuals:
        coeff_dict["residual_lowpass"] = energy["residual_lowpass"]
        coeff_dict["residual_highpass"] = energy["residual_highpass"]

    return coeff_dict
