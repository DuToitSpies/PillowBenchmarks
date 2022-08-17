from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

jpg1 = Image.open("../../testImages/python.jpeg")
jpg1 = jpg1.resize((400,400))
jpg1.putalpha(1)
jpg2 = Image.open("../../testImages/boomslang.jpeg")
jpg2 = jpg2.resize((400,400))
jpg2.putalpha(1)
outfile = open("output/" + impl + "_" + api, "w")

for i in range(100):
    start_time = timeit.default_timer()
    for i in range(100):
        im = Image.alpha_composite(jpg1, jpg2)
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
