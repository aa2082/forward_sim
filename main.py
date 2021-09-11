from PIL import Image
from PIL import ImageDraw
import numpy as np
from cell import make_cell

import time
start = time.time()

img_dim = 3200 #pixel dimensions of image, more the longer to render
hwa_lab_xy_max = 18
multiplication_factor = img_dim/(2*hwa_lab_xy_max)
hwa_lab_r = 0.5
syn_r = multiplication_factor*hwa_lab_r
#np array that will be image, initially all set to 0 ie black
bw_data = np.zeros((img_dim,img_dim), dtype=np.uint8)

#L indicates mode: (8-bit pixels, black and white)
#https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

cells = np.genfromtxt('test_e1e2.txt', delimiter=' ')
print(cells)
cells = (cells*multiplication_factor)+img_dim/2
print(cells)
num_cells = np.shape(cells)[0]
for i in range(1,num_cells):
    print(i)
    make_cell(bw_data,(img_dim,img_dim),cells[i,:],syn_r)
bw = Image.fromarray(bw_data, 'L') #make image from array
bw.show() #show image

end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))
