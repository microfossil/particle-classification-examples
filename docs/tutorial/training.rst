Training Overview
=================

The MISO particle classification library consists of python scripts to make training convolutional neural networks easier.

Networks
--------

There are a variety of CNN topologies that can be used, and two different methods of training, transfer learninging and full network:

**Transfer learning** uses a pre-trained CNN to generate feature vectors for each image which are then uses as the input to a simple, non-convolutional NN. The pre-trained CNN and simple NN are then combined to give a CNN model that takes images as input. This method is *very fast* to train but does not use augmentation, although the accuracy is very good. It is recommended to start here.

The options are:

* **resnet50_tl**: Transfer learning using ResNet50 CNN trained on ImageNet weights

**Normal training** trains an entire CNN from scratch. There are multiple topologies to choose from, and augmentation is used during training. This method takes much longer to train than for transfer learning, however the accuracy is usually slightly better. The options for topologies are:

* **base_cyclic**: This CNN was designed at CEREGE for Foraminifera training. The design is a smaller version of VGG but with cyclic layers and batch normalisation. The size of the network adapts to the specified input image size. It is the fastest of the normal training options. 

* **resnet18 / resent34 / resnet50**: Residual network with 18 / 34 / 50 layers. It features skip connections so that small image features can bypass the network and go straight to the later stages. The network gives good accuracy. Larger sizes take longer to train.

* **vgg16 / vgg19**: The classic VGG design. It has largely been superceeded.

.. tip::

   We recommend starting with transfer learning, then trying base_cyclic and resnet34 to get an idea if training the full network gives a significant improvement in accuracy.

Training
--------

Training of the network is performed using a portion of the dataset (75%) with the remainder kept aside to evaluate its accuracy. Once training has begun, the performance (loss measure) of the CNN on the training set is monitored. If it has not improved for a certain number of epochs (complete runs through the training data) the internal learning rate (how much the weights in the CNN are allowed to change with each training step) is dropped by half. After a certain number of these drops, training is stopped.

For normal training, the images are augmented at each step with the following transformations, to simulate normal microscope variations:

* rotation
* gain (brightness)
* gamma (contrast)
* bias (offset)

Result
------

The output of training is:

* A frozen model of the trained CNN that can be used for classification, either via python scripts or ParticleTrieur.
* An xml file containing metadata about the CNN and training results.
* Graphs of training results such as accuracy, precision and recall.
* An estimate of which images in the dataset may have been mislabeled during dataset creation.
