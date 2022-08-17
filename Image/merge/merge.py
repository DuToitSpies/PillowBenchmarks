from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

jpg1 = Image.open("../../testImages/python.jpeg")
r, g, b = jpg1.split()
outfile = open("output/" + impl + "_" + api, "w")

for i in range(100):
    start_time = timeit.default_timer()
    for i in range(100):
        im = Image.merge("RGB", b, g, r)
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
