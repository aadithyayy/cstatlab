import numpy as np

rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))

print(f"Enter {rows*cols} elements:")
matrix=np.array(list(map(int,input().split()))).reshape(rows,cols)

eigenval,eigenvect=np.linalg.eig(matrix)

print("Eigen Values:\n",eigenval)
print("Eigen Vector:\n",eigenvect)