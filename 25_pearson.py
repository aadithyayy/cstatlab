import numpy as np

arr1=np.array(list(map(int,input("Enter array 1:").split())))
arr2=np.array(list(map(int,input("Enter array 2:").split())))
arr1=arr1.reshape(2,2)
arr2=arr2.reshape(2,2)

print("Array 1:\n",arr1)
print("Array 2:\n",arr2)
cormatrix=np.corrcoef(arr1,arr2)
print("Correlation Matrix:\n",cormatrix)
print("Correlation Coefficient: ", cormatrix[0,1])