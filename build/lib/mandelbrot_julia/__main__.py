from .Mandelbrot import plot_mandelbrot, plot_Julia
import argparse

def main_mandel():
    parser = argparse.ArgumentParser(description="Fractal Plotter")
    parser.add_argument("--zmin", default = -2 -1.5j, type = complex, help = "zmin to define borders")
    parser.add_argument("--zmax", default = 0.5 + 1.5j, type = complex, help = "zmax to define borders")
    parser.add_argument("--pixel_size", type = float, default = 1/512)
    parser.add_argument("--max_iter", default = 50, type = int, help = "maximal number of iterations")
    parser.add_argument("--o", default = "figure.png", help = "name of the figure")
    args = parser.parse_args()

    plot_mandelbrot(args.zmin, args.zmax, args.pixel_size, args.max_iter, args.o)




def main_julia():
    parser = argparse.ArgumentParser(description="Fractal Plotter")
    parser.add_argument("--c", default = -0.8 + 0.156j, type=complex, help="Complex constant for Julia set (default: -0.8+0.156j)")
    parser.add_argument("--zmin", default=-2 -1j , type = complex, help = "zmin to define borders")
    parser.add_argument("--zmax", default = 2 + 1j,type = complex, help = "zmax to define borders")
    parser.add_argument("--pixel_size", type = float,default = 1/(512*4))
    parser.add_argument("--max_iter", default = 100, type = int, help = "maximal number of iterations")
    parser.add_argument("--o", default = "figure.png", help = "name of the figure")
    args = parser.parse_args()

    
    plot_Julia(args.c, args.zmin, args.zmax, args.pixel_size, args.max_iter, args.o)



