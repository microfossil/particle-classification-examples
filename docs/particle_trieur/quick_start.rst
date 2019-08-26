Quick Start
===========

The following tutorial gives a quick start to the typical ParticleTrieur workflow:

* Start a new project and add images.
* Add labels for the classes you wish to classify.
* Export the labeled images.
* Launch training.
* Load the trained network and use it to classify unlabeled images.

Before beginning for the first time, please read the tutorial on :doc:`../tutorial/dataset_creation` to understand what to consider when creating a training dataset.

Start up
--------

1. Launch ParticleTrieur and select *New Project* in the startup window.

.. image:: ../images/software/startup.png

2. After a few seconds to load, the main window will show.

* At the top is a toolbar of commonly used commands
* On the left is a table which lists all the added images
* On the right there are three tabs:

    * Classification: Manual labeling of images and prediction using either the built in AI or and external CNN.
    * Similarity: The most similar images to the currently selected image.
    * Processing: Methods for processing the images, e.g. brightness normalisation.

.. image:: ../images/software/startup_main.png

Add images
----------

1. Click *Add* to start adding images. The add dialog will pop up.

.. image:: ../images/software/add_images.png

2. In the dialog that pops up select to add by folder (all images in the folder and sub-folder will be added) or by image (select one or multiple images) then click *Choose...* to select the folder / images.

3. Click "OK" to add the images, then *Close* on the progress dialog once it is finished.

4. The *Edit Metadata* dialog will pop up.

.. image:: ../images/software/add_images.png

5. Enter any metadata associated with the images (leave blank if unknown):

* Sample: The name of the sample from which the images were taken.
* Index 1: The primary numerical index for which the images can be sorted (e.g. starting core depth for foraminifera).
* Index 2: The secondary numerical index for which the images can be sorted (e.g. end core depth for foraminifera)
* Resolution: The resolution of the images in pixels per millimeter.

6. Click "OK" to update the metadata, then *Close* on the progress dialog once it is finished.

Feature vector
--------------

ParticleTrieur automatically calculates a *feature vector* for every image. The feature vector is like a finger print of the image, and similar images have similar vectors. The feature vector is used for k-NN classification and for the similary tab.

The progress of the feature vector calculation is shown in the top right corner of the screen:

.. image:: ../images/software/post_adding.png

Also whenever there is a significant change to the project, the save button will be highlighted in red, to remind you the project needs saving.

Save the project
----------------

1. Save the project by clicking *Save* and choosing a save location.

.. Important:: 

    The location of the added images is saved in the project file as a relative path to the project file, except if they are on an external drive (Windows), in which they are saved as absolute paths.  

    This means that the project file is moved, the images must be moved with it, to keep the same relative structure. **We recommend storing the project file in the parent directory (or same directort) of the images** to make this easier.

The project is saved as a plain-text XML file. You can edit it manually if desired.

Add labels
----------

Add a label for each of the classes you wish to identify:

1. In the classification tab, click the *+ Add* button in the *Labels* section. 

2. Enter the code, name and description of the label

* Code: This is the text that will identify the label. It will appear on the label button and be used as the class name for CNN training. We recommend either a short, memorable code or the full name in the format `genus_species` (i.e. no spaces). Whatever, the code, it should be consistant across projects!

* Name: The name of the class the label refers to, e.g. a full taxonomic classification (optional).

* Description: Further details of the class (optional).

.. image:: ../images/software/add_label.png

3. Click *OK*.

4. Repeat steps 1-3 for the remaining labels. After this is complete, there will be one button for each label in the *Labels* section.

.. Note::

    To edit or delete a label, right-click the label button and click *Edit...* or *Delete...* in the pop-up dialog.

Label images
------------

1. Label an image by selecting it from list on the left then clicking the corresponding label button

.. image:: ../images/software/post_add_label.png

.. Tip:: 

    Enable *Auto-advance* to have ParticleTrieur automatically move on to the next image after the label button is clicked.

The in-built *k-NN prediction* system will automatically predict which label belongs to an image using the previously labeled images and their feature vectory.

It does this by looking at the top N (usually 12) most-similar images *that have already been labeled* to the selected image, and assigning a score to each label based on the number of images in that label in the top N.

The scores are shown as red bars across the top of the label buttons, and the best prediction is indicated by a symbol.

.. image:: ../images/software/knn_score.png

.. Note::

    The k-NN prediction only considers images that have already been labeled. Therefore, it will not be accurate until enough images from each class have been labeled. 
