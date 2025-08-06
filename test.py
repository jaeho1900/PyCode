import numpy as np

array1 = np.arange(18)
array2 = array1.reshape(2,3,3, order='F')
array2.flatten()
