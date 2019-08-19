"""
Example image classification with the MISO library
"""
from miso.training.model_params import default_params
from miso.training.model_trainer import train_image_classification_model

params = default_params()

# OVERVIEW -------------------------------------------------------------------------------------------------------------
# A short name to describe the network
# The name will be also be used to construct the output directory name

params['name'] = 'image_classification_example'

# Longer description of the network
# The longer description will be saved in the xml description of the network
# Set to None to be auto-generated

params['description'] = None

# CNN TOPOLOGY ---------------------------------------------------------------------------------------------------------
# The type of network
# Choices are:
# Network       Description
# -----------   -----------------------------------------------------------------------
# base_cyclic   Classic sequential layer CNN with cyclic layers and batch normalisation
# resnet18      Residual network (uses skip connections) with 18 layers
# resnet34      Residual network with 34 layers
# resnet50      Residual network with 50 layers
# resnet50_tl   Transfer learning using ResNet50 (VERY FAST)

params['type'] = 'resnet50_tl'

# Base Cyclic configurable parameters
# The base_cyclic network is a custom design and can be configured further
# - filters: 4, 8, 16, 32, etc. More filters may improve accuracy.
params['filters'] = 4
# - use batch normalisation: True / False. Batch normalisation typically improves accuracy.
params['use_batch_norm'] = True
# - global pooling: None, 'avg', 'max'
params['global_pooling'] = None
# - activation: 'relu', 'elu', 'selu'
params['activation'] = 'relu'

# The input dimensions of the image
# For height and width:
# - height and width should be the same for particle images to ensure proper rotation augmentation
# - 128 x 128 works well for simple particles
# - 224 x 224 is the size ResNet has been designed for
# - height and width will automatically be set when using transfer learning
# - NOTE: Larger images take longer to train!
# For number of channels:
# - using channels = 1 will convert the images to greyscale (recommended if colour is not a feature)
# - using channels = 3 will leave the image in RGB mode

params['img_height'] = 128
params['img_width'] = 128
params['img_channels'] = 1

# TRAINING -------------------------------------------------------------------------------------------------------------
# Number of images presented per training iteration
# 64 is recommended. Lower to 32 or 16 if getting out-of-memory errors

params['batch_size'] = 64

# Maximum epochs after which training is definitely stopped
# Keep at a high number like 10000 as training will normally
# be stopped by the adaptive learning rate system

params['max_epochs'] = 10000

# Number of epochs and drops for the adaptive learning rate system. (ALR)
# ALR will monitor the last alr_epochs worth of epochs during training.
# If the loss is not decreasing, the learning rate will be dropped by half.
# After alr_drops times of drops, training is stopped.

params['alr_epochs'] = 40
params['alr_drops'] = 4


# AUGMENTATION ---------------------------------------------------------------------------------------------------------
# Use augmentation (transfer learning automatically sets this to false)
params['use_augmentation'] = False

# INPUT ----------------------------------------------------------------------------------------------------------------
# Input data source
# Either a local directory, e.g. r'C:\Users\my_name\Documents\Data\particle_training_set\'
# or a direct download link, e.g. r'https://1drv.ws/u/s!AiQM7sVIv7fah4MN2gWCXDWX_DT0OA?e=Eu3lZh'

params['input_source'] = r'https://1drv.ws/u/s!AiQM7sVIv7fah4MN2gWCXDWX_DT0OA?e=Eu3lZh'

# Minimum number of images per class for that class to be included
# Recommended that this value is at least 20

params['data_min_count'] = 40

# Fraction of images used for testing to calculate accuracy etc

params['data_split'] = 0.25

# Weight the classes by count
# If the number of images in each class varies significantly, training may try to improve accuracy by maximising the
# over-represented classes at the expense of the under-represented. Using class weights will weight the
# under-represented classes more highly, usually improving their accuracy.

params['use_class_weights'] = True

# OUTPUT ---------------------------------------------------------------------------------------------------------------
# Root directory to save trained model, graphs etc.(A sub-directory will be automatically created for each training run)
# Can be an absolute path, e.g. r'C:\Users\my_name\Documents\TrainedModels\'
# Or a relative path to the directory from which this script was run, e.g. r'output'

params['output_dir'] = r'output'

# What format to save the trained model in
# frozen: Frozen format used for inference (recommended)
# saved_model: Tensorflow Saved Model format (graph and weights in separate files)
# None: Don't save a model

params['save_model'] = 'frozen'

# Whether to estimate mislabeled images or not
# params['save_mislabeled'] = True

# RUN ------------------------------------------------------------------------------------------------------------------
# model: Trained Keras model for image classification in inference mode
# vector_model: Sub-graph of previous model for generating feature vectors
# data_source: The training data
# results: Results of training (accuracy, precision, recall, f1score, etc)

model, vector_model, data_source, results = train_image_classification_model(params)
