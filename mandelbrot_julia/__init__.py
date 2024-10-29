from .Mandelbrot import plot_mandelbrot, plot_Julia

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fractal Plotter")
    parser.add_argument("fractal", choices=["mandelbrot", "julia"], help="Fractal type to plot")
    parser.add_argument("--c", type=complex, default=-0.8 + 0.156j, help="Complex constant for Julia set (default: -0.8+0.156j)")

    args = parser.parse_args()

    if args.fractal == "mandelbrot":
        plot_mandelbrot()
    elif args.fractal == "julia":
        plot_Julia(args.c)
