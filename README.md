# Image classification using the MISO library

The MISO library was created to provide a simplified interface to help create, train and save convolutional neural networks (CNNs) for image classification, in particular for particle images such as foraminifera.

In allows the training of popular networks such as ResNet, as well as a custom CNN design created at CEREGE, "base cyclic", that gives good accuracy with fast training time for particle images. The library also performs dataset augmentation, such as rotation, brightness, gamma, and zoom, during training, as these are the variances most often encountered in microscope images.

The trained networks are saved in a frozen model format, allowing them to be used to perform classification, for example, in our ForamTrieur software.

This repository contains some Jupyter notebooks and python scripts to demonstrate training using the MISO library. They can be used as a base for writing your own scripts.

## Tutorial

Google Colab is a free online service for running python scripts and training neural networks using the Tensorflow library.

We have created a tutorial in the form of a Jupyter notebook to describe how to start training a network with MISO.

[Click here to open the notebook in Google Colab](https://colab.research.google.com/github/microfossil/particle-classification-examples/blob/master/image_classification_with_miso_tutorial.ipynb)
