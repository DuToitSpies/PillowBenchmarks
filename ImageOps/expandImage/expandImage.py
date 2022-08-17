from PIL import Image, ImageOps


import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

jpg = "../testImages/python.jpeg"
outfile = open("output/" + impl + "_" + api, "w")

for i in range(1000):
    im = Image.open(jpg)
    start_time = timeit.default_timer()
    for i in range(100):
        im2 = ImageOps.expand(im, 100, 100)
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
