from setuptools import setup, find_packages

setup(
    name="mandelbrot_julia_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "fractal-plot=mandelbrot_julia:main",
        ],
    },
    description="A package to plot Mandelbrot and Julia sets.",
)
