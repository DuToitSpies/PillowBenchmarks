from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

im1 = Image.new('RGBA',(400,400))
im2 = Image.new('RGBA',(400,400))
outfile = open("output/" + impl + "_" + api, "w")

for i in range(100):
    start_time = timeit.default_timer()
    for i in range(100):
        im = Image.alpha_composite(im1, im2)
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
