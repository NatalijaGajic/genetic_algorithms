import numpy as np
v = np.random.randn(10)
print(v)
maximum = np.max(v)
minimum = np.min(v)
print(maximum, minimum)

index_of_maximum = np.where(v == maximum)
index_of_minimum = np.where(v == minimum)
print(v[index_of_minimum])
