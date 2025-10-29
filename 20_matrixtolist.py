import numpy as np
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of cols:"))

print(f"Enter {rows * cols} elements separated by spaces:")
elements = list(map(int, input().split()))

matrix = np.array(elements).reshape(rows, cols)
print(matrix)

flat=matrix.flatten().tolist()
print(flat)