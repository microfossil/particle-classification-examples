[Open tutorial in Google Colab](https://colab.research.google.com/github/microfossil/particle-classification-examples/blob/master/image_classification_with_miso_tutorial.ipynb)

[Open script in Google Colab](https://colab.research.google.com/github/microfossil/particle-classification-examples/blob/master/image_classification_with_miso_quick.ipynb)

[Download ParticleTrieur](https://particle-classification.readthedocs.io/en/latest/)

# Image classification using the MISO library

The MISO library was created to provide a simplified interface to help create, train and save convolutional neural networks (CNNs) for image classification, in particular for particle images such as foraminifera.

In allows the training of popular networks such as ResNet, as well as a custom CNN design created at CEREGE, "base cyclic", that gives good accuracy with fast training time for particle images. The library also performs dataset augmentation, such as rotation, brightness, gamma, and zoom, during training, as these are the variances most often encountered in microscope images.

The trained networks are saved in a frozen model format, allowing them to be used to perform classification, for example, in our ForamTrieur software.

This repository contains some Jupyter notebooks and python scripts to demonstrate training using the MISO library. They can be used as a base for writing your own scripts.

## Documentation

In-depth documentation covering installing software, creating a training set, configuring a network, and performing training is described [here.](https://particle-classification.readthedocs.io/en/latest/)

##  Google Colab 

We recommend starting by reading the documentation, but if you want to jump straight in, please follow out tutorial in Google Colab.

Google Colab is a free online service for running python scripts and training neural networks using the Tensorflow library. We have created a tutorial Jupyter notebook for Google Colab that takes you step-by-step through training a network wiht MISO. Running the notebook and training is done online, and therefore you do not need your own GPU.

If you don't have a Google account already, please sign up, then [click here to open the notebook in Google Colab](https://colab.research.google.com/github/microfossil/particle-classification-examples/blob/master/image_classification_with_miso_tutorial.ipynb)

For experienced users, there is a slimmed down notebook without the tutorial clutter [here.](https://colab.research.google.com/github/microfossil/particle-classification-examples/blob/master/image_classification_with_miso_quick.ipynb)
