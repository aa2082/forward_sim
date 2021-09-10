from PIL import Image
from PIL import ImageDraw
import numpy as np
from cell import make_cell

img_dim = 320 #pixel dimensions of image
hwa_lab_xy_max = 40
multiplication_factor = img_dim/(2*hwa_lab_xy_max)
hwa_lab_r = 0.5
syn_r = multiplication_factor*hwa_lab_r
#np array that will be image, initially all set to 0 ie black
bw_data = np.zeros((img_dim,img_dim), dtype=np.uint8)

#L indicates mode: (8-bit pixels, black and white)
#https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

myFile = np.genfromtxt('30.csv', delimiter=' ')
cells = myFile[:,[3,4,6,7]]
cells = (cells*multiplication_factor)+img_dim/2
num_cells = np.shape(cells)[0]
for i in range(1,num_cells):
    print(i)
    make_cell(bw_data,(img_dim,img_dim),cells[i,:],syn_r)
bw = Image.fromarray(bw_data, 'L') #make image from array
bw.show() #show image
