import numpy as np

rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))

print(f"Enter {rows*cols} elements")
matrix=np.array(list(map(int,input().split()))).reshape(rows,cols)

q,r=np.linalg.qr(matrix)
print("Ortho:\n",q)
print("Uptrian:\n",r)

print(np.allclose(matrix, q @ r))
