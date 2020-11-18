Installation
============


MISO
----

CNN training can either be performed locally or using Google Colab.

Local installation
``````````````````

1. Install Anaconda from `here <https://www.anaconda.com/distribution/>`_. Use the default installation options, making sure that *Install for: Just me* is selected.

2. Open the Anaconda command prompt (Windows) or terminal (MacOS).

3. Create a new python environment called *miso*:

``conda create -n miso python=3.7``

4. Activate the *miso* environment:

``conda activate miso``

5. Install Tensorflow v1.14, the version depends on if you have an NVIDIA GPU:

With GPU: ``conda install tensorflow-gpu=1.14``

Without GPU: ``conda install tensorflow=1.14``

6. Install the MISO library:

``pip install -U git+https://github.com/microfossil/particle-classification``

Setup is complete!

To update the MISO library in the future, perform steps 2, 4 and 6, or click the *Update Library* button in the *Training* dialog in ParticleTrieur


ParticleTrieur
--------------

