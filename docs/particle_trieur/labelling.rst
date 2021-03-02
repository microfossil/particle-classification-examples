Classification and Labelling
============================

The right side of the main window has tabs for labelling, processing and viewing the parameters of the particles. The `classification` and `similarity` tabs are used for labelling the images.

* The classification tab is used for directly labelling the images or estimating the image label using either k nearest neighbours (kNN) or an already trained convolutional neural network (CNN)
* The similarity tab displays particles that are similar to the currently selected particle

.. image:: /images/pt/classification-window.png

Labelling
---------

Particle images are labelled according to their class or status. The choice of labels is up to user. There are two types of labels:

* **Class labels** are labels that will be used to train a CNN. For example, those corresponding to species or morphological classes. 
* **Non-class labels** are labels that are NOT used to train a CNN. Applying a non-class label means the image is not classified yet. There are two default non-class labels:
   * **Unlabeled** is the default label of newly added images. It means the image has not been labeled.
   * **Unsure** is the label given to an image when an automatic classifier, e.g. kNN or CNN, cannot confidently predict the particle's class.

Adding labels
`````````````

To add a label, select :guilabel:`Edit` > :guilabel:`Edit`

Buttons
```````

Particles can be labelled and / or tagged using the buttons in the Classification tab. 


.. list-table:: 

   * - List view
     - Grouped view
     - Tree view
   * - .. image:: /images/pt/classification-buttons-1.png
     - .. image:: /images/pt/classification-buttons-2.png
     - .. image:: /images/pt/classification-buttons-3.png
   



