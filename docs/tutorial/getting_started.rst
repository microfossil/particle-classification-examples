Getting Started
===============

Convolutional neural network (CNN) based classification systems are currently the state-of-the-art in image classification, outperforming previous methods based on engineered features.

The procedure to create a CNN using our software is:

1. **Creation:** Create an dataset consisting of a wide variety of images of all the different classes you wish to identify. The images should span the range of normal variations you would expect to see in each class.

2. **Labeling:** Label the images according to their class. This can be done manually by sorting into directories, or AI-assisted with our ParticleTrieur software.

3. **Training:** Train a CNN using the labeled images. CNN training is computationally expensive and takes a long time on a normal laptop without high-powered graphics card, so we instead have prepared some scripts for training in the cloud using the free Google Colab service.

4. **Validation:** The training scrpits produce graphs of the accuracy of the network, as well as estimating if any images have been mislabeled. We use these results to tweak the CNN parameters or double-check the image labeling, respectively.

5. **Inference:** The final output of training is a *frozen* CNN which can now be used for classifying unknown images! There are two ways to use the CNN: via the command line with a python script, or by loading into our ParticleTrieur software.

ParticleTrieur is not absolutely necessary to make and use a CNN, but we recommend it as part of a normal laboratory workflow.