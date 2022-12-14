from PIL import Image
from timeit import default_timer as dt
import sys, os

impl = sys.implementation.name
api = sys.argv[1]

im = Image.new("RGB", (400,400))
out = open("output/"+impl+"_"+api, "w")

for i in range(100):
    start = dt()
    for j in range(100):
        im.resize((100,100))
        im.resize((400,400))
    out.write(str(dt()-start)+"\n")

out.close()
