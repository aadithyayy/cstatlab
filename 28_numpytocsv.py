import numpy as np

arr=np.arange(9).reshape(3,3)
np.savetxt("misc.csv",arr,fmt="%d",delimiter=",")

