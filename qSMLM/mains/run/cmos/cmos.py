import numpy as np

nx,ny = 7,7
gain = 2.2*np.ones((nx,ny))
offset = 100*np.ones((nx,ny))
var = 5.0*np.ones((nx,ny))

np.savez('gain.npz',gain)
np.savez('offset.npz',offset)
np.savez('var.npz',var)
