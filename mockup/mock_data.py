import sys
import os

benchmark = sys.argv[1]

datapath = "../Image/"+benchmark+"/output/"

infile = open(datapath+"cpython_hpy")

pypy_out = open(datapath+"pypy_MOCKUP", "w")
graal_out = open(datapath+"graal_MOCKUP", "w")

for line in infile:
    val = float(line)
    pypy_out.write(str(val/2)+"\n")
    graal_out.write(str(val/3)+"\n")

pypy_out.close()
graal_out.close()