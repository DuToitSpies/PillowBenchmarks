import sys
import os

import matplotlib.pyplot as plt
import numpy as np

benchmark = sys.argv[1]
num_bins = int(sys.argv[2])
min_bin = float(sys.argv[3])
max_bin = float(sys.argv[4])
comparison = sys.argv[5]

datafiles = []
data = []
binvals = []
bins = []
comparisons = ["hpy", "capi", "cpython", "pypy", "graalpython"]
labels = []

datapath = "../"+benchmark+"/output/"
outfiles = os.listdir(datapath)

for output in outfiles:
    labels.append(output)
    if comparison in output:
        datafiles.append(output)
        data.append([])
        binvals.append(np.zeros(num_bins))


for i in range(len(datafiles)):
    f = open(datapath+datafiles[i])
    for line in f:
        line.strip()
        data[i].append(float(line))

for i in range(num_bins):
    bins.append(round(min_bin+i/num_bins*(max_bin-min_bin), 5))

for i in range(len(data)):
    for j in data[i]:
        databin = int((j - min_bin)/max_bin*num_bins)
        if databin > num_bins-1:
            databin = num_bins-1
        elif databin < 0:
            databin = 0
        binvals[i][databin] = binvals[i][databin]+1

plt.hist(data[0], bins, color='red', label=labels[0])
plt.hist(data[1], bins, color='blue', label=labels[1])
plt.hist(data[2], bins, color='green', label=labels[2])
plt.xlabel("Time [s]")
plt.ylabel("Frequency")
plt.title("Histogram of benchmark performance of the Pillow copy method written in HPy and the C-API  on CPython")
plt.legend()
plt.show()
