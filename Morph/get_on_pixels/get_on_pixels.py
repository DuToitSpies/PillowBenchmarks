from PIL import ImageMorph, Image
import timeit
import sys

impl = sys.implementation.name
api = sys.argv[1]

im1 = Image.open('../../testImages/bwpython.jpeg')
out = open('output/'+impl+'_'+api, 'w')

lut = ImageMorph.LutBuilder('1:(....1.1.1)->1')
mo = ImageMorph.MorphOp(lut=lut)

for i in range(100):
    start_time = timeit.default_timer()
    for j in range(1):
        mo.get_on_pixels(im1)
    print(timeit.default_timer()-start_time)
