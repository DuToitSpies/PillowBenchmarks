from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

im1 = Image.open("../../testImages/python.jpeg")
outfile = open("output/" + impl + "_" + api, "w")

for i in range(100):
    start_time = timeit.default_timer()
    for i in range(200):
        im2 = im1.copy()
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
