Particle Classification
=======================

Welcome to the help and tutorial documentation for the ParticleTrieur program and the MISO python library.

Overview
--------

MISO
....

MISO is a library of python scripts that simplify training a CNN from a set of labeled images. A variety of common CNN topologies can be chosen, such as variations of ResNet or using transfer learning. The scripts take a folder of images and output a trained model along with statistics on the model performance. The system is optimised for particle images.

`Github repository <https://github.com/microfossil/particle-trieur>`_

ParticleTrieur
..............

**ParticleTrieur** is a cross-platform java program to help organise, label, process and classify images, particularly for particle samples such as microfossils. It can be used for both the creation of the training set required to make a CNN classifier, and classification of image using a trained CNN. It also includes some image processing functions, morphology calculations and statistical graph generation. ParticleTrieur allows the user to configure and launch training using the MISO library.

ParticleTrier is release under the open-source GPL v2 licence and the source code can be found at `Github repository <https://github.com/microfossil/particle-trieur>`_

Getting started
---------------

- `Read <introduction>`_ the introduction on ParticleTrieur, MISO and how to create a good training set for CNN models.
- `Install <installation>`_ ParticleTrieur and MISO


Citing
------

If using ParticleTrieur with the MISO library please cite our paper on CNNs for foraminifera classification at the `Journal of Micropalaeontology <https://jm.copernicus.org/articles/39/183/2020/>`_

::

    @article{jm-39-183-2020,
       author = {Marchant, R and Tetard, M and Pratiwi, A and Adebayo, M and de Garidel-Thoron, T},
       doi = {10.5194/jm-39-183-2020},
       journal = {Journal of Micropalaeontology},
       number = {2},
       pages = {183--202},
       title = {{Automated analysis of foraminifera fossil records by image classification using a convolutional neural network}},
       url = {https://jm.copernicus.org/articles/39/183/2020/},
       volume = {39},
       year = {2020}
    }


Table of contents
=================

.. toctree::
   :caption: Getting started

   introduction
   installation

.. toctree::
   :caption: ParticleTrieur

   particle_trieur/overview
   particle_trieur/add-images
   particle_trieur/sorting


.. Overview
.. --------
.. Automated classification of images can improve efficiency in the laboratory, particularly for tedious manual tasks such as counting particle types (e.g. foraminifera morphotypes) from microscope slides.

.. .. image:: images/particles/U_peregrina.png
..    :width: 100px

.. .. image:: images/particles/B_pagoda.png
..    :width: 100px

.. .. image:: images/particles/B_spissa.png
..    :width: 100px

.. .. image:: images/particles/G_affinis.png
..    :width: 100px

.. .. image:: images/particles/Planktic.png
..    :width: 100px

.. We have created two pieces of software to enable researchers to create and use their own automatic classification system based on convolutional neural networks (CNNs):



.. .. image:: images/software/particle-trieur.png
..    :width: 600px

.. A computer with a high-powered graphics card is not necessary for training the CNNs, we will use **google colab** to perform training in the cloud.

.. :doc:`Click here to get started! <tutorial/getting_started>`


.. `Download ParticleTrieur 2.2.0 for all platforms <https://github.com/microfossil/particle-trieur/releases>`_


.. .. toctree::
..    :maxdepth: 1
..    :caption: Tutorial:

..    tutorial/getting_started
..    tutorial/dataset_creation
..    tutorial/training
..    tutorial/training_2
..    tutorial/inference

.. .. toctree::
..    :maxdepth: 1
..    :caption: ParticleTrieur:

..    particle_trieur/overview
..    particle_trieur/quick_start

.. .. Indices and tables
.. .. ==================

.. .. * :ref:`genindex`
.. .. * :ref:`modindex`
.. .. * :ref:`search`
