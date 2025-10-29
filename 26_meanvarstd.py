import numpy as np

values=np.array(list(map(float,input("Enter list of values:").split())))

print("Values:",values)
print("Mean: ",np.mean(values))
print("Variance: ",np.var(values))
print("Standard Deviation: ",np.std(values))