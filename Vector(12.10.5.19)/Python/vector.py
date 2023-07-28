import numpy as np 
import matplotlib.pyplot as plt 
from numpy import linalg as LA 
import math

a = (np.pi)/4
O = np.array(([0, 0])) 
A = np.array(([1, 0])) 
B = np.array(([1, 1]))

def line_gen(A,B):
   len =2
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB

#Generating all lines
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)

#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:],label='a')
plt.plot(x_OB[0,:],x_OB[1,:],label='b')

plt.text(0.5, 0.03, 'a')
plt.text(0.56, 0.6, 'b')


#Labeling the coordinates
tri_coords = np.vstack((O,A,B)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (tri_coords[0, i], tri_coords[1, i]), textcoords="offset points",
                 xytext=(0, 10), ha='center')



plt.xlabel('$X-Axis$')
plt.ylabel('$Y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('Angle between Dot and Cross Product',size=15)
plt.text(-0.1,0,'(0,0)')
plt.text(1,0,'(1,0)')
plt.text(0.8,1,'(1,1)')

#if using termux
plt.savefig('/sdcard/Documents/Python/figs/vector')
plt.show()
