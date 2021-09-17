from PIL import Image
from PIL import ImageDraw
import numpy as np
from cell import make_cell

import time
start = time.time()

img_dim = 2000 #pixel dimensions of image, more the longer to render
xy_max = 20
multiplication_factor = img_dim/(xy_max*2)
print(multiplication_factor, " pixels/µm")
cell_r = .5
syn_r = multiplication_factor*cell_r
#np array that will be image, initially all set to 0 ie black
bw_data = np.zeros((img_dim,img_dim), dtype=np.uint8)

#L indicates mode: (8-bit pixels, black and white)
#https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

cells = np.genfromtxt('test_e1e2.txt', delimiter='   ')
cells = (cells*multiplication_factor)+img_dim/2
num_cells = np.shape(cells)[0]
for i in range(1,num_cells):
    percent = (int)((i/num_cells)*100)
    print(percent,"%")
    make_cell(bw_data,(img_dim,img_dim),cells[i,:],syn_r)
bw = Image.fromarray(bw_data, 'L') #make image from array
bw.show() #show image

end = time.time()
print(multiplication_factor, " pixels/µm")
print("Elapsed (after compilation) = %s" % (end - start))
