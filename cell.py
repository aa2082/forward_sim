import numpy as np
from numba import jit

@jit(nopython=True)
def make_cell(data,img_dim,coord,r):
    #e1,e2: vectors from 0,0 to poles
    e1 = np.array([coord[0],coord[1],0])
    e2 = np.array([coord[2],coord[3],0])
    n = e2 - e1
    len_n = np.linalg.norm(n)
    unit_n = n/len_n
    # not sure if i should do something else than int casting in range function
    for i in range(int(max(0,min(coord[0],coord[2])-r)),int(min(img_dim[0],max(coord[0],coord[2])+r))):
         for j in range(int(max(0,min(coord[1],coord[3])-r)),int(min(img_dim[1],max(coord[1],coord[3])+r))):
            p = np.array([i,j,0])
            m = p - e1
            dot = np.dot(m,unit_n)
            if(dot<=0): #case 1
                a = np.linalg.norm(p - e1)
                if(a<r):
                    data[i,j] = (np.sqrt((r**2)-(a**2))/r)*255
            elif(dot<len_n):
                a = np.linalg.norm(np.cross(m,unit_n))
                if(a<r):
                    data[i,j] = (np.sqrt((r**2)-(a**2))/r)*255
            elif(dot>=len_n):
                a = np.linalg.norm(p - e2)
                if(a<r):
                    data[i,j] = (np.sqrt((r**2)-(a**2))/r)*255
