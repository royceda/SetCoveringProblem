import numpy as np;


x = np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])

size = x.shape

print "test : ", x[1, : ]

print "norm : ", np.linalg.norm(x[:,1]);

print "before : ", x

x = np.delete(x, 0, axis=0)

print "after : ", x

x = np.delete(x, 2, axis=1)

print "after : ", x
