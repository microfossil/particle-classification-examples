.. _installation:

Installation
============

ParticleTrieur
--------------

ParticleTrieur is distributed as a Java JAR file. It requires the installation of Java 8 to run.

1. Install `Amazon Corretto 8 <https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/downloads-list.html>`_ or another Java 8 JRE / JDK
2. Test the java installation by opening command prompt (Windows) or terminal (macOS) and running `java -version`. It should return something like:

::

    C:\Users\rossm>java -version
    openjdk version "1.8.0_212"
    OpenJDK Runtime Environment Corretto-8.212.04.2 (build 1.8.0_212-b04)
    OpenJDK 64-Bit Server VM Corretto-8.212.04.2 (build 25.212-b04, mixed mode)

2. Download the latest release of ParticleTrier.jar from the `github repostory releases page <https://github.com/microfossil/particle-trieur/releases>`_
3. Save the JAR file in a convient location

To run ParticleTrieur:

1. Open command prompt (Windows) or terminal (macOS / linux)
2. Change directory to the one containing ParticleTrieur.jar

::

    cd /PATH/TO/PARTICLETRIEUR

3. Execute the jar file

    Windows / Linux:

::

    java -jar ParticleTrieur.jar

    MacOS:

::

    java -jar ParticleTrieur.jar -Djava.awt.headless=true


.. note::

    The latest version of ParticleTrieur may be called ParticleTrieur-dev.jar or similar. Update the instructions above accordingly.

MISO
----

The MISO library is required to perform CNN training using ParticleTrieur but can also be used stand alone.

1. Install Anaconda from `here <https://www.anaconda.com/distribution/>`_. Use the default installation options, making sure that *Install for: Just me* is selected.
2. Open the Anaconda command prompt (Windows) or terminal (MacOS / Linux).
3. Create a new python environment called *miso2*:

::

    conda create -n miso2 python=3.7

4. Activate the *miso2* environment:

::

    conda activate miso2

5. Install Tensorflow v1.14, the version depends on if you have an NVIDIA GPU:

With GPU:

::

    conda install tensorflow-gpu==1.15
    pip install tensorflow-gpu==1.15.2

Without GPU:

::

    conda install tensorflow=1.15
    pip install tensorflow==1.15.2

6. Install the MISO library:

::

    pip install miso2

Setup is complete!

To update the MISO library in the future, perform steps 2, 4 and 6, or click the *Update Library* button in the *Training* dialog in ParticleTrieur




