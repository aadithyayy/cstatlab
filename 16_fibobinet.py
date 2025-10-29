import numpy as np

phi=(1+np.sqrt(5))/2
psi=(1-np.sqrt(5))/2

n=10

fib=(((phi**np.arange(n))-(psi**np.arange(n)))/np.sqrt(5))
print(fib.astype(int))