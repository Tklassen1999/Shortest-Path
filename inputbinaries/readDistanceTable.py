import numpy as np

cityCount =6
filename = "spp6.bin"
cityMap = np.fromfile(filename,  dtype=np.int, count = -1)
cityMap = np.reshape(cityMap,(cityCount,cityCount))
print(cityMap)
