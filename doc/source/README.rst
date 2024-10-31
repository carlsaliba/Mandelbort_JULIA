Mandelbrot and Julia Set Plotting
=================================

This project demonstrates how to plot the Mandelbrot and Julia sets using Python, Matplotlib, and Pillow.

Table of Contents
-----------------
- `Introduction <#introduction>`_
- `Requirements <#requirements>`_
- `Installation <#installation>`_
- `Usage <#usage>`_
- `Examples <#examples>`_
- `License <#license>`_

Introduction
------------

The Mandelbrot set is a set of complex numbers that produces a particular type of fractal when plotted. The Julia set is closely related and is derived from the Mandelbrot set by fixing a complex number and varying the initial value.

Requirements
------------

To run the scripts for plotting the Mandelbrot and Julia sets, you will need:

- Python 3.x
- Matplotlib
- NumPy
- Pillow

Installation
------------

1. **Clone or download the repository**:

   Clone the repository or download the source code, then navigate to the project directory.

   .. code-block:: bash

       git clone <repository_url>
       cd <repository_folder>

2. **Install the package**:

   Use the following command to install the package in editable mode. Make sure you are in the project directory.

   .. code-block:: bash

       pip install -e .

Usage
-----

Once installed, you can use the following commands to generate Mandelbrot and Julia set images.

- **For Mandelbrot set**:

  .. code-block:: bash

      MandelbrotPlot

  .. image:: ../figure.png
   :alt: Example Mandelbrot Plot
   :width: 600px

- **For Julia set**:

  .. code-block:: bash

      JuliaPlot
  .. image:: ../figure_julia.png
   :alt: Example Mandelbrot Plot
   :width: 600px
Examples
--------

To generate more specific fractal images, you can use these examples:

- **Mandelbrot plot with custom parameters**:

  .. code-block:: bash

      MandelbrotPlot --zmin="-0.7440+0.1305j" --zmax="-0.7425+0.1320j" --pixel_size=5e-7 --max_iter=200 --o=Mandelbrot_tentacle.png

- **Julia plot with custom parameters**:

  .. code-block:: bash

      JuliaPlot --c=-0.8j --pixel_size=1e-3 --max_iter=50 --o "thunder-julia.png"

Each command generates an image of the respective set with the specified parameters.

License
-------

This project is licensed under the MIT License.
