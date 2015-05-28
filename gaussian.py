import numpy

def generate_gaussian(center, height, width):
    def gaussian(x):
        return height*numpy.exp(-((x-center)/width)**2)
    return gaussian

def generate_spectrum(*peaks, **kwargs):
    shift=kwargs.get('shift', 0)
    gaussians = [generate_gaussian(c+shift, h, w) for c, h, w in peaks]
    def spectrum(x):
        return sum([g(x) for g in gaussians])
    return spectrum
            


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('centers', type=float, nargs='+', help='Center')
    parser.add_argument('--common-height', type=float, default=1.0, help='Height')
    parser.add_argument('--common-width', type=float, default=0.01, help='Width')
    parser.add_argument('--step', type=float, default=0.01, help='Width')
    parser.add_argument('--output', default='plot.dat', help='Output file')
    parser.add_argument('--shift', type=float, default=0.0, help='Shift')

    args = parser.parse_args()

    minx = min(args.centers) - 2*args.common_width
    maxx = max(args.centers) + 2*args.common_width

    x = numpy.arange(minx, maxx, args.step)
    peaks = tuple([(c,args.common_height,args.common_width) for c in args.centers])
    g = generate_spectrum(*peaks, shift=arg.shift)
    with open(args.output, 'w') as f:
        for x, y in zip(x, g(x)):
            f.write("%f %f\n" %(x, y))
        
        
