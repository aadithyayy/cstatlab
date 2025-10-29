import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

print("Inner:",np.inner(a,b))
print("Outer:\n",np.outer(a,b))
print("Cross:",np.cross(a,b))