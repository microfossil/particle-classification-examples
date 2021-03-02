Selection and Sorting
=====================

Particle images added to the project appear on the left side of the main window:

.. image:: /images/pt/selection-1.png

There are three tabs:

- Images presented in a list view
- Images presented in a grid view
- A single large image of the currently select image

Above the three tabs is the filtering input box

Below the three tabs is a :guilabel:`Select All` button for convieniently selecting all the images and two buttons for decreasing / increasing the size of the images in the list and grid views.


List view
---------

.. image:: /images/pt/selection-list-view.png

The list view contains a thumbnail image of the particle and the main metadata parameters. The columns are:

- **#:** Image number in project
- **Image:** Image thumbnail
- **Sample:** Sample name and indicies
  
  - 1st line: sample name
  - 2nd line: index 1 value
  - 3rd line: index 2 value
   
- **Label/Tag:** The label and tags of the image
  
  - 1st line: label
  - 2nd line: list of tags
  - 3rd line: the validation status - blank if not validated, green tick if validated
  
- **Annotator:** Username of person who labeled the image, and optionally, who validated it.
  
  - 1st line: label username
  - 2nd line: validator username
   
- **Filename:** Filename of image
- **Folder:** Folder where the file is stored
- **Resolution:** Resolution of the image in pixels per millimetre
- **GUID:** Globally unique identifier of the image

Use the Shift and Ctrl (Command on macOS) keys to select multiple images.


Grid view
---------

.. image:: /images/pt/selection-grid-view.png

The grid view contains a thumbnail image of the particle with the image number in the project and its label. If the image has been validated, a green tick will appear in the top right corner.

Use the Shift and Ctrl (Command on macOS) keys to select multiple images.

.. note::
   
   Right-clicking on an image will show a larger version of it with more metadata.


Image view
----------

.. image:: /images/pt/selection-image-view.png

The image view contains a large size image of the (first) selected image(s) along with the image metadata.


Filtering
---------

The filtering input box can be used to filter the list of images according to their metadata. Multiple filtering options can be concatenated to narrow down the results.

The possible filtering fields are:

- ``#`` (image number)
- ``sample``
- ``label``
- ``tag``
- ``index1``
- ``index2``
- ``file``
- ``folder``
- ``guid``
- ``valid`` (if the image has been validated, use true or false)

The possible filtering operators are:

- ``==`` contains
- ``!=`` does not contain
- ``===`` exact match
- ``!==`` not an exact match

Enter a combination of fields to filter the list, for example:

- ``label==fragment`` returns all images with the label *fragment* as part of their name, e.g.*fragment_round* or *fragment_bilobal*.
- ``label===fragment`` returns all the images with label *fragment* exactly.
- ``label!=fragment valid==true`` returns all the images whose label does not contain *fragment* and have been validated.

.. important::

   Values with spaces in them need to be replaced with underscores '_'. For example, if you wish to filter for images with label *fragment round* then the filter would be ``label==fragment_round``

.. image:: /images/pt/filter.png