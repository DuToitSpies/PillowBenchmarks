import matplotlib.pyplot as plt
import os
import sys
import numpy as np

benchmarks = sys.argv[1].split(",")
num_bins = sys.argv[2].split(",")
min_bins = sys.argv[3].split(",")
max_bins = sys.argv[4].split(",")

fig, axes = plt.subplots(3, 3)
fig.suptitle("Histograms of benchmark performance of the Pillow methods written in HPy on CPython, PyPy, and GraalPython, and in the C-API  on CPython")
fig.subplots_adjust(hspace=0.4)

j = 0

for i in range(len(benchmarks)):
    benchmark = benchmarks[i]

    datapath = "../Image/"+benchmark+"/output/"
    outfiles = os.listdir(datapath)

    inum_bins = int(num_bins[0])
    imin_bin = float(min_bins[0])
    imax_bin = float(max_bins[0])

    datafiles = []
    data = []
    binvals = []
    bins = []

    labels = ['CPython (C API)', 'CPython (HPy)', 'PyPy (HPy) (Data is not real)', 'GraalPython (HPy) (Data is not real)']
    outfiles = ["cpython_capi", "cpython_hpy", "pypy_MOCKUP", "graal_MOCKUP"]

    for output in outfiles:
        datafiles.append(output)
        data.append([])
        binvals.append(np.zeros(inum_bins))

    for i in range(len(datafiles)):
        f = open(datapath+datafiles[i])
        for line in f:
            line.strip()
            data[i].append(float(line))

    for i in range(inum_bins):
        bins.append(round(imin_bin+i/inum_bins*(imax_bin-imin_bin), 5))

    print(inum_bins)
    print(bins)

    axes[j][0].hist(data[0], bins, color='gray', alpha=0.75, label=labels[0])
    axes[j][0].hist(data[1], bins, color='blue', alpha=0.75, label=labels[1])
    axes[j][0].set(xlabel="Time [s]", ylabel="Frequency")
    axes[j][0].legend()

    axes[j][1].hist(data[0], bins, color='gray', alpha=0.75, label=labels[0])
    axes[j][1].hist(data[2], bins, color='green', alpha=0.75, label=labels[2])
    axes[j][1].set(xlabel="Time [s]", ylabel="Frequency")
    axes[j][1].legend()
    axes[j][1].set_title("The " + benchmark + " method")

    axes[j][2].hist(data[0], bins, color='gray', alpha=0.75, label=labels[0])
    axes[j][2].hist(data[3], bins, color='orange', alpha=0.75, label=labels[3])
    axes[j][2].set(xlabel="Time [s]", ylabel="Frequency")
    axes[j][2].legend()

    j = j+1

plt.show()