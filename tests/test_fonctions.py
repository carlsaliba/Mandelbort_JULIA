import unittest

from mandelbrot_julia import is_in_Mandelbrot, is_in_Julia  # Import the functions from your main file

class TestFunctions(unittest.TestCase):

    def test_mandel(self):
        self.assertTrue(is_in_Mandelbrot(0.251, 20), "La fonction doit renvoyer True")
        self.assertFalse(is_in_Mandelbrot(0.251, 100), "La fonction doit renvoyer False")

    def test_julia(self):
        self.assertTrue(is_in_Julia(z = 0.25 +0.25j, c = 0.25, num_iterations = 100), "La fonction doit renvoyer True")
       

if __name__ == "__main__":
    unittest.main()
