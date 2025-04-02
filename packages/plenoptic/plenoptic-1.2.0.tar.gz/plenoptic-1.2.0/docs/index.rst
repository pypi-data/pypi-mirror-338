.. |pypi-shield| image:: https://img.shields.io/pypi/v/plenoptic.svg
			 :target: https://pypi.org/project/plenoptic/

.. |conda-shield| image:: https://anaconda.org/conda-forge/plenoptic/badges/version.svg
                  :target: https://anaconda.org/conda-forge/plenoptic

.. |license-shield| image:: https://img.shields.io/badge/license-MIT-yellow.svg
                    :target: https://github.com/plenoptic-org/plenoptic/blob/main/LICENSE

.. |python-version-shield| image:: https://img.shields.io/badge/python-3.10%7C3.11%7C3.12-blue.svg

.. |build| image:: https://github.com/plenoptic-org/plenoptic/workflows/build/badge.svg
		     :target: https://github.com/plenoptic-org/plenoptic/actions?query=workflow%3Abuild

.. |zenodo| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.10151130.svg
            :target: https://zenodo.org/doi/10.5281/zenodo.10151130

.. |codecov| image:: https://codecov.io/gh/plenoptic-org/plenoptic/branch/main/graph/badge.svg?token=EDtl5kqXKA
             :target: https://codecov.io/gh/plenoptic-org/plenoptic

.. |binder| image:: https://mybinder.org/badge_logo.svg
		    :target: https://mybinder.org/v2/gh/plenoptic-org/plenoptic/1.2.0?filepath=examples

.. plenoptic documentation master file, created by
   sphinx-quickstart on Thu Jun 20 15:56:27 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


plenoptic
*********
.. _index:

|pypi-shield| |conda-shield| |license-shield| |python-version-shield| |build| |zenodo| |codecov| |binder|


.. image:: images/plenoptic_logo_wide.svg
   :align: center
   :alt: plenoptic logo

``plenoptic`` is a python library for model-based synthesis of perceptual stimuli. For ``plenoptic``, models are those of visual [1]_ information processing: they accept an image as input, perform some computations, and return some output, which can be mapped to neuronal firing rate, fMRI BOLD response, behavior on some task, image category, etc. The intended audience is researchers in neuroscience, psychology, and machine learning. The generated stimuli enable interpretation of model properties through examination of features that are enhanced, suppressed, or discarded. More importantly, they can facilitate the scientific process, through use in further perceptual or neural experiments aimed at validating or falsifying model predictions.


Getting started
---------------

- If you are unfamiliar with stimulus synthesis, see the :ref:`conceptual-intro`
  for an in-depth introduction.
- Otherwise, see the `Quickstart <tutorials/00_quickstart.nblink>`_
  tutorial.

Installation
^^^^^^^^^^^^

The best way to install ``plenoptic`` is via ``pip``::

$ pip install plenoptic

or ``conda``::

$ conda install plenoptic -c conda-forge

.. warning::  We do not currently support conda installs on Windows, due to the lack of a Windows pytorch package on conda-forge. See `here <https://github.com/conda-forge/pytorch-cpu-feedstock/issues/32>`_ for the status of that issue.

See the :ref:`install` page for more details, including how to set up an isolated
virtual environment (recommended).

ffmpeg and videos
^^^^^^^^^^^^^^^^^

Some methods in this package generate videos. There are several backends
available for saving the animations to file (see `matplotlib documentation
<https://matplotlib.org/stable/api/animation_api.html#writer-classes>`_
).
To convert them to HTML5 for viewing (for example, in a
jupyter notebook), you'll need `ffmpeg <https://ffmpeg.org/download.html>`_
installed. Depending on your system, this might already
be installed, but if not, the easiest way is probably through `conda
<https://anaconda.org/conda-forge/ffmpeg>`_: ``conda install -c conda-forge
ffmpeg``.
To change the backend, run ``matplotlib.rcParams['animation.writer'] = writer``
before calling any of the animate functions. If you try to set that ``rcParam``
with a random string, ``matplotlib`` will list the available choices.


.. _package-contents:
Contents
--------

.. figure:: images/example_synth.svg
   :figwidth: 100%
   :alt: The four synthesis methods included in plenoptic

Synthesis methods
^^^^^^^^^^^^^^^^^

- `Metamers <tutorials/intro/06_Metamer.nblink>`_: given a model and a reference image,
  stochastically generate a new image whose model representation is identical to
  that of the reference image (a "metamer", as originally defined in the literature on Trichromacy).
  This method makes explicit those features that the model retains/discards.

  - Example papers: [Portilla2000]_, [Freeman2011]_, [Deza2019]_,
    [Feather2019]_, [Wallis2019]_, [Ziemba2021]_
- `Eigendistortions <tutorials/intro/02_Eigendistortions.nblink>`_: given a model and a
  reference image, compute the image perturbations that produce the smallest/largest
  change in the model response space. These are the
  image changes to which the model is least/most sensitive, respectively.

  - Example papers: [Berardino2017]_
- `Maximal differentiation (MAD) competition
  <tutorials/intro/08_MAD_Competition.nblink>`_: given a reference image and two models that measure distance
  between images, generate pairs of images that optimally
  differentiate the models. Specifically, synthesize a pair of images that are equi-distant from
  the reference image according to model-1, but maximally/minimally distant according to model-2.  Synthesize
  a second pair with the roles of the two models reversed. This method allows
  for efficient comparison of two metrics, highlighting the aspects in which
  their sensitivities most differ.

  - Example papers: [Wang2008]_

Models, Metrics, and Model Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Steerable pyramid, [Simoncelli1992]_ and [Simoncelli1995]_, a multi-scale
  oriented image decomposition. Images are decomposed with a family of oriented
  filters, localized in space and frequency, similar to the "Gabor functions"
  commonly used to model receptive fields in primary visual cortex. The critical
  difference is that the pyramid organizes these filters so as to effeciently
  cover the 4D space of (x,y) positions, orientations, and scales, enabling
  efficient interpolation and interpretation (`further info
  <https://www.cns.nyu.edu/~eero/STEERPYR/>`_ ). See the `pyrtools documentation
  <https://pyrtools.readthedocs.io/en/latest/index.html>`_ for more details on
  python tools for image pyramids in general and the steerable pyramid in
  particular.
- Portilla-Simoncelli texture model, [Portilla2000]_, which computes a set of image statistics
  that capture the appearance of visual textures (`further info <https://www.cns.nyu.edu/~lcv/texture/>`_).
- Structural Similarity Index (SSIM), [Wang2004]_, is a perceptual similarity
  metric, that takes two images and returns a value between -1 (totally different) and 1 (identical)
  reflecting their similarity (`further info <https://www.cns.nyu.edu/~lcv/ssim>`_).
- Multiscale Structural Similarity Index (MS-SSIM), [Wang2003]_, is an extension of SSIM
  that operates jointly over multiple scales.
- Normalized Laplacian distance, [Laparra2016]_ and [Laparra2017]_, is a
  perceptual distance metric based on transformations associated with the early
  visual system: local luminance subtraction and local contrast gain control, at
  six scales (`further info <https://www.cns.nyu.edu/~lcv/NLPyr/>`_).

Getting help
------------

We communicate via several channels on Github:

- To report a bug, open an `issue
  <https://github.com/plenoptic-org/plenoptic/issues>`_.
- To send suggestions for extensions or enhancements, please post in the `ideas
  section
  <https://github.com/plenoptic-org/plenoptic/discussions/categories/ideas>`_
  of discussions first. We'll discuss it there and, if we decide to pursue it,
  open an issue to track progress.
- To ask usage questions, discuss broad issues, or
  show off what you've made with plenoptic, go to `Discussions
  <https://github.com/plenoptic-org/plenoptic/discussions>`_.
- To contribute to the project, see the `contributing guide
  <https://github.com/plenoptic-org/plenoptic/blob/main/CONTRIBUTING.md>`_.

In all cases, we request that you respect our `code of conduct
<https://github.com/plenoptic-org/plenoptic/blob/main/CODE_OF_CONDUCT.md>`_.

Citing us
---------

If you use ``plenoptic`` in a published academic article or presentation, please
cite us! See the :ref:`citation` for more details.

.. toctree::
   :titlesonly:
   :caption: Basic concepts
   :glob:

   install
   jupyter
   conceptual_intro
   models
   tutorials/*
   citation

.. toctree::
   :titlesonly:
   :glob:
   :caption: Synthesis method introductions

   tutorials/intro/*

.. toctree::
   :titlesonly:
   :glob:
   :caption: Models and metrics

   tutorials/models/*

.. toctree::
   :titlesonly:
   :glob:
   :caption: Synthesis method examples

   tutorials/applications/*

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Advanced usage

   synthesis
   tips
   reproducibility
   API Documentation <api/modules>
   tutorials/advanced/*

.. [1] These methods also work with auditory models, such as in `Feather et al.,
       2019
       <https://proceedings.neurips.cc/paper_files/paper/2019/hash/ac27b77292582bc293a51055bfc994ee-Abstract.html>`_
       though we haven't yet implemented examples. If you're interested, please
       post in `Discussions
       <https://github.com/plenoptic-org/plenoptic/discussions)>`_!

.. [Portilla2000] Portilla, J., & Simoncelli, E. P. (2000). A parametric texture
   model based on joint statistics of complex wavelet coefficients.
   International journal of computer vision, 40(1), 49–70.
   https://www.cns.nyu.edu/~lcv/texture/.
   https://www.cns.nyu.edu/pub/eero/portilla99-reprint.pdf
.. [Freeman2011] Freeman, J., & Simoncelli, E. P. (2011). Metamers of the
   ventral stream. Nature Neuroscience, 14(9), 1195–1201.
   https://www.cns.nyu.edu/pub/eero/freeman10-reprint.pdf
.. [Deza2019] Deza, A., Jonnalagadda, A., & Eckstein, M. P. (2019). Towards
   metamerism via foveated style transfer. In , International Conference on
   Learning Representations.
.. [Feather2019] Feather, J., Durango, A., Gonzalez, R., & McDermott, J. (2019).
   Metamers of neural networks reveal divergence from human perceptual systems.
   In NeurIPS (pp. 10078–10089).
.. [Wallis2019] Wallis, T. S., Funke, C. M., Ecker, A. S., Gatys, L. A.,
   Wichmann, F. A., & Bethge, M. (2019). Image content is more important than
   bouma's law for scene metamers. eLife. https://dx.doi.org/10.7554/elife.42512
.. [Berardino2017] Berardino, A., Laparra, V., J Ball\'e, & Simoncelli, E. P.
   (2017). Eigen-distortions of hierarchical representations. In I. Guyon, U.
   Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, & R. Garnett,
   Adv. Neural Information Processing Systems (NIPS*17) (pp. 1–10). : Curran
   Associates, Inc. https://www.cns.nyu.edu/~lcv/eigendistortions/
   https://www.cns.nyu.edu/pub/lcv/berardino17c-final.pdf
.. [Wang2008] Wang, Z., & Simoncelli, E. P. (2008). Maximum differentiation
   (MAD) competition: A methodology for comparing computational models of
   perceptual discriminability. Journal of Vision, 8(12), 1–13.
   https://ece.uwaterloo.ca/~z70wang/research/mad/
   https://www.cns.nyu.edu/pub/lcv/wang08-preprint.pdf
.. [Simoncelli1992] Simoncelli, E. P., Freeman, W. T., Adelson, E. H., &
   Heeger, D. J. (1992). Shiftable Multi-Scale Transforms. IEEE Trans.
   Information Theory, 38(2), 587–607. https://dx.doi.org/10.1109/18.119725
.. [Simoncelli1995] Simoncelli, E. P., & Freeman, W. T. (1995). The steerable
   pyramid: A flexible architecture for multi-scale derivative computation. In ,
   Proc 2nd IEEE Int'l Conf on Image Proc (ICIP) (pp. 444–447). Washington, DC:
   IEEE Sig Proc Society. https://www.cns.nyu.edu/pub/eero/simoncelli95b.pdf
.. [Wang2004] Wang, Z., Bovik, A., Sheikh, H., & Simoncelli, E. (2004). Image
   quality assessment: from error visibility to structural similarity. IEEE
   Transactions on Image Processing, 13(4), 600–612.
   https://www.cns.nyu.edu/~lcv/ssim/.
   https://www.cns.nyu.edu/pub/lcv/wang03-reprint.pdf
.. [Wang2003] Z Wang, E P Simoncelli and A C Bovik. Multiscale structural
   similarity for image quality assessment Proc 37th Asilomar Conf on Signals,
   Systems and Computers, vol.2 pp. 1398--1402, Nov 2003.
   https://www.cns.nyu.edu/pub/eero/wang03b.pdf
.. [Laparra2017] Laparra, V., Berardino, A., Johannes Ball\'e, &
   Simoncelli, E. P. (2017). Perceptually Optimized Image Rendering. Journal of
   the Optical Society of America A, 34(9), 1511.
   https://www.cns.nyu.edu/pub/lcv/laparra17a.pdf
.. [Laparra2016] Laparra, V., Ballé, J., Berardino, A. and Simoncelli,
   E.P., 2016. Perceptual image quality assessment using a normalized Laplacian
   pyramid. Electronic Imaging, 2016(16), pp.1-6.
   https://www.cns.nyu.edu/pub/lcv/laparra16a-reprint.pdf
.. [Ziemba2021] Ziemba, C.M., and Simoncelli, E.P. (2021). Opposing effects of selectivity and invariance in peripheral vision.
   Nature Communications, vol.12(4597).
   https://dx.doi.org/10.1038/s41467-021-24880-5

This package is supported by the `Center for Computational Neuroscience <https://www.simonsfoundation.org/flatiron/center-for-computational-neuroscience/>`_,
in the Flatiron Institute of the Simons Foundation.

.. image:: images/CCN-logo-wText.png
   :align: center
   :alt: Flatiron Institute Center for Computational Neuroscience logo
