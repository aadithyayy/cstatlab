sparse={}
matrix=[]
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))

print("Enter matrix row by row:")
for i in range(rows):
    row=list(map(int, input().split()))
    matrix.append(row)
    for j in range(cols):
        if row[j]!=0:
            sparse[(i, j)] = row[j]

print("Original matrix:")
for row in matrix:
    print(row)
print("Sparse Matrix")
print(sparse)