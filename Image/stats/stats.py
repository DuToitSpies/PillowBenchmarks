import numpy as np
import sys, os

benchmark = sys.argv[1]

datapath = "../"+benchmark+"/output/"
datafiles = os.listdir(datapath)

out = open("../"+benchmark+"/stats.txt", "w")

datafiles.sort()

for file in datafiles:
    name = str(file)
    filedata = open(datapath + name)
    vals = []
    for line in filedata:
        vals.append(float(line))
    npvals = np.array(vals)
    mean = np.mean(npvals)
    std = np.std(npvals)
    out.write(name + "\t" + str(mean) + "+/-" + str(std)+"\n")