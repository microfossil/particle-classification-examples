Running Training
================

Normal training of a CNN is very computationally intensive and requires a high-powered NVIDA graphics card (GPU) for it to complete in a reasonable time. For example, a large 20000 image dataset may take over 2 hours to train on the ResNet50 CNN on a top-of-the-line consumer NVIDIA 2080 Ti GPU. On a typical laptop, training could be 50 times slower.

Transfer learning is much faster as the computationally intensive parts (convolutions) are only calculated once. This method is recommended on a normal computer without a high-powered GPU.

There are four methods for performaing training, explained below. 

We recommend the Google Colab method for those without a GPU. Google Colab provides a cloud-based python environment with a high-powered GPU, and can be used for free to train CNNs. 

.. note:: Please follow the tutorial on Google Colab method the first time.

Google Colab
------------

Google Colab is an online cloud-based Jupyter notebook environment and provides a high-powered GPU free for use. 

We have written a detailed tutorial on training a CNN on Google Colab using the MISO library. It shows how to upload the dataset and run the training. We recommended to follow this tutorial the first time, regardless, as it explains all the training options in detail.

`Click here <https://colab.research.google.com/github/microfossil/particle-classification-examples/blob/master/image_classification_with_miso_tutorial.ipynb>`_ to open the tutorial notebook in Google Colab.

For experienced users, a concise version of the notebook without the tutorial explanations is `here <https://colab.research.google.com/github/microfossil/particle-classification-examples/blob/master/image_classification_with_miso_quick.ipynb>`_.


Local Python Installation
-------------------------

The MISO library can also be run locally. 

Setup
`````

Python, Tensorflow and the MISO library must be installed. We recommend using the Anaconda python distribution system.

1. Install Anaconda from `here <https://www.anaconda.com/distribution/>`_. Use the default installation options, making sure that *Install for: Just me* is selected.

2. Open the Anaconda command prompt. 

3. Create a new python environment called *miso*:

   ``conda create -n miso python=3.7``

4. Activate the *miso* environment:

   ``conda activate miso``

5. Install ``tensorflow-gpu`` if you have a supported NVIDIA GPU, otherwise install ``tensorflow``:

   With GPU: ``conda install tensorflow-gpu=1.14``

   Without GPU: ``conda install tensorflow=1.14``

6. Install the MISO library:

   ``pip install -U git+https://github.com/microfossil/particle-classification``

Setup is complete!

To update the MISO library in the future, perform steps 2, 4 and 6.

Creating a script
`````````````````

An example training script can be found here.


