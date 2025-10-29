import numpy as np

arr=np.arange(27).reshape(3,3,3)
print("Original Array:\n",arr,"\n")

diag=np.diagonal(arr,axis1=-1,axis2=-2)
print("Diagonals:\n",diag,"\n")

