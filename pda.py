from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import eig
img1=Image.open('1im.gif','r')
img2=Image.open('2im.gif','r')
img3=Image.open('3im.gif','r')
img4=Image.open('4im.gif','r')
#img1=Image.open('1im.gif').convert('L')
#img2=Image.open('2im.gif').convert('L')
#img3=Image.open('3im.gif').convert('L')
#img4=Image.open('4im.gif').convert('L')
val1=np.array(img1.getdata())
val2=np.array(img2.getdata())
val3=np.array(img3.getdata())
val4=np.array(img4.getdata())
arr1=np.reshape(val1,(512*512,1))
arr2=np.reshape(val2,(512*512,1))
arr3=np.reshape(val3,(512*512,1))
arr4=np.reshape(val4,(512*512,1))
a=np.zeros(512*512*4).reshape(512*512,4)
for j in range(0,512*512):
      a[j][0]=arr1[j][0]
      a[j][1]=arr2[j][0]
      a[j][2]=arr3[j][0]
      a[j][3]=arr4[j][0]
print(np.cov(a))