from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

im1 = Image.new('L',(500,500))
outfile = open("output/" + impl + "_" + api, "w")

for i in range(200):
    start_time = timeit.default_timer()
    for i in range(300):
        im2 = im1.crop((33,103,140,410))
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
