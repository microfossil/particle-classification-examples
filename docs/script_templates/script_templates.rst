from miso.training.model_params import default_params
from miso.training.model_trainer import train_image_classification_model
from miso.data.download import download_images

params = default_params()

params['type'] = resnet18
params['name'] = 
params['description'] = None
params['input_dir'] = r'C:\Users\rossm\Documents\Data\Foraminifera\EndlessForamsExported\images_20190808_132035'
params['data_min_count'] = 40
params['data_split'] = 0.250000
params['output_dir'] = r'C:\Users\rossm\Documents\Data\Foraminifera\EndlessForamsExported'
params['save_model'] = frozen
params['save_mislabeled'] = True
params['img_height'] = 128
params['img_width'] = 128
params['img_channels'] = 3
params['use_augmentation'] = True
params['use_class_weights'] = True
params['alr_epochs'] = 40
params['batch_size'] = 64

model, data_source, result = train_image_classification_model(params)
