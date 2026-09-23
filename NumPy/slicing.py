import numpy as np
q1=np.array([
    [2,3,4],
    [5,6,7],
    [8,9,10]
])
q2=np.array([
    [2,3,4],
    [5,6,7],
    [8,9,10]
])
print(np.vstack((q1,q2))) #horizontal stacking
index=np.argmax(q1) #maximum value at which index
print(index)