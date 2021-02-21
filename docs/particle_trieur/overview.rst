Overview
========

The primary functions of ParticleTrieur (PT) are:

* Organise images according to their sample, resolution and other metadata.
* Label images by their taxonomic class, and tag them according to their properties.
* Use in-built AI to help predict the label of an image based on the most similar already labeled images.
* Load a external trained convolutional neural network (CNN) to help label images.
* Process particle images, such as by removing borders, normalising intensity, or centering the particle in the image.
* Calculate morphology information such as circularity or solidity. 
* Export images, by processing them and sorting them into directories by their label.
* See graphs of statistics such as label counts.
* Configure and launch CNN training with the MISO particle classification library.

.. _glossary:

Glossary
--------

PT allows the organisation of particle images according to their metadata. PT projects are saved in human-readable XML format.

A project consists of settings data and a list of particle metadata. The particle metadata is:

- **Filename**: The path to the image. This will be *relative to the project file* if saved on the same drive as the project file, otherwise it will be absolute. `Path (wikipedia) <https://en.wikipedia.org/wiki/Path_(computing)>`_
- **Sample**: The name of the sample from which the image was taken.
- **Index 1**: An index value used to sort images and generate statistics. For example, if index 1 may be set to the depth at which a foraminifera sample was taken.
- **Index 2**: A secondary index.
- **Resolution**: The resolution of the image in pixels per millimetre.
- **GUID:**: A globally unique identifier for the image.
- **Classifications**: Labels and their confidence scores for this image, along with the **id** of the classifier. When manually labelling and image there will be only a single classification with the score set to 1.0. The classification items consist of two values:
  
  - **code:** The classification label code of the class.
  - **score:** The confidence score of the classification [0-1].
  
- **Tags:** Tags to help sort images, see below.
- **Validator:** The name of the person who validated the image label.
- **Morprhology:** The calculated morphology of the particle.
- **Parameters:** All other metadata for the particle.

The project metadata also contains a list of labels used for classification and tags:

- **Labels:** Labels are the names of the various classes to which an image can be assigned. There are also non-taxonomic labels such as `unlabeled` and `unsure` which are used for images that have not been labelled or cannot be identified confidently. Taxonomic labels are used to train the CNN model.
- **Tags:** Tags are used to help sort the images, but are not used in CNN training. There are some build in tags such as *auto*, which is given to images that are automatically classified by a CNN or other, and *duplicate* which is given to images identified as duplicates by the *Find duplicates...* command.


Launching PT
------------

If not already installed, follow the instructions in :ref:`installation`

1. Open command prompt (Windows) or terminal (macOS / linux)
2. Change directory to the one containing ParticleTrieur.jar

::

    cd /PATH/TO/PARTICLETRIEUR

3. Execute the jar file

::

    java -jar ParticleTrieur.jar

The startup window will show:

.. image:: /images/pt/startup.png

On the left:

- **New project** will start a new project with the default settings
- **New project from template** will prompt to open an existing project, from which a new project will be created with no images but using the same settings.
- **Open project** will prompt to open and existing project.

On the right:

**Recent projects** show as list of up to the last 5 opened projects.

Main Window
-----------

Choosing and option will start the program after a moment to load the internal AI algorithms. On the left is a list of particles and their metadata, on the right are the labelling and processing tools and common functions are on a toolbar at the top.

.. image:: /images/pt/main.png

