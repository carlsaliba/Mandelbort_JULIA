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
        if abs(z) > 2:
            return False
    
    return True

def is_in_Julia(z, c, num_iterations):
    """
    Détermine si un point complexe `z` appartient à l'ensemble de Julia pour un 
    nombre complexe donné `c`, en vérifiant s'il reste borné après un certain nombre 
    d'itérations.

    Paramètres:
    - z (complex): Point complexe initial.
    - c (complex): Constante complexe définissant l'ensemble de Julia.
    - num_iterations (int): Nombre d'itérations (terme de la suite).

    Retourne:
    - bool: True si `z` est dans l'ensemble, sinon False.
    """
    for _ in range(num_iterations):
        z = z ** 2 + c
        if abs(z) > 2 :
            return False
    
    return True



def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    """
    Génère une matrice de nombres complexes correspondant aux coordonnées
    dans la zone définie par (xmin, xmax, ymin, ymax) et à la densité de pixels 
    spécifiée.

    Paramètres:
    - xmin (float): Limite minimale sur l'axe réel.
    - xmax (float): Limite maximale sur l'axe réel.
    - ymin (float): Limite minimale sur l'axe imaginaire.
    - ymax (float): Limite maximale sur l'axe imaginaire.
    - pixel_density (int): Densité de pixels pour l'échantillonnage.

    Retourne:
    - np.ndarray: Matrice de nombres complexes correspondant aux coordonnées.
    """
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def plot_mandelbrot(zmin = -2 -1.5j, zmax = 0.5 + 1.5j, pixel_size = 1/512, max_iter= 50, o = "figure.png"):
    """
    Génère et affiche une image de l'ensemble de Mandelbrot dans une fenêtre graphique.

    Paramètres:
    - Aucun.

    Retourne:
    - None: Affiche directement l'image de l'ensemble de Mandelbrot.
    """

   
    c = complex_matrix( zmin.real, zmax.real, zmin.imag, zmax.imag, pixel_density=1/pixel_size)
    mandelbrot_set = np.vectorize(is_in_Mandelbrot)(c, num_iterations=max_iter)
    image_array = np.logical_not(mandelbrot_set) * 255
    image = Image.fromarray(image_array.astype(np.uint8))
    image.save(o)
    image.show()
    
    




def plot_Julia(c= -0.8 + 0.156j, zmin = -2 -1j, zmax = 2 + 1j, pixel_size = 1/(512*4), max_iter= 100, o = "figure.png"):
    """
    Génère et affiche une image de l'ensemble de Julia dans une fenêtre graphique.

    Paramètres:
    - c (complex): Constante complexe définissant l'ensemble de Julia.

    Retourne:
    - None: Affiche directement l'image de l'ensemble de Julia.
    """
    
    z = complex_matrix(zmin.real, zmax.real, zmin.imag, zmax.imag, pixel_density=1/pixel_size)
    julia_set = np.vectorize(lambda z: is_in_Julia(z, c, num_iterations=max_iter))(z)
    image_array = np.logical_not(julia_set) * 255
    image = Image.fromarray(image_array.astype(np.uint8))
    image.save(o)
    image.show()
    


