import cmath
import numpy as np
from PIL import Image



def is_in_Mandelbrot(c, num_iterations):
    """
    Détermine si un nombre complexe `c` appartient à l'ensemble de Mandelbrot 
    en vérifiant s'il reste borné après un certain nombre d'itérations.

    Paramètres:
    - c (complex): Nombre complexe à tester.
    - num_iterations (int): Nombre d'itérations (terme de la suite) .

    Retourne:
    - bool: True si `c` est dans l'ensemble, sinon False.
    """
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2


def is_in_Julia(z,c, num_iterations):
    

    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j



def plot_mandelbrot():
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
    mandelbrot_set = is_in_Mandelbrot(c, num_iterations=20)
    
    

    # Use np.logical_not to invert the mask
    image_array = np.logical_not(mandelbrot_set) * 255
    image = Image.fromarray(image_array.astype(np.uint8))
    image.show()
    return


def plot_Julia(c):
    z = complex_matrix(-2, 2, -1, 1, pixel_density=512*4)
    julia_set = is_in_Julia(z,c, num_iterations=100)
    
    

    # Use np.logical_not to invert the mask
    image_array = np.logical_not(julia_set) * 255
    image = Image.fromarray(image_array.astype(np.uint8))
    image.show()
    return








