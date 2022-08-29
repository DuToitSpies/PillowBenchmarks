from PIL import Image
import sys, os
from timeit import default_timer as dt

impl = sys.implementation.name
api = sys.argv[1]

im = Image.new('RGBA', (400,400))
out = open("output/"+impl+"_"+api, "w")

for i in range(100):
    start = dt()
    for j in range(500):
        im2 = im.copy()
    out.write(str(dt() - start) + "\n")

out.close()