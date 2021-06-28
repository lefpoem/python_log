import numpy as np
import matplotlib.pyplot as plt
np.random.seed(19680801)
y = np.random.normal(loc=0.5,scale=0.4,size=50)
y = y[(y>0) & (y<1)]
y.sort()
x = np.array(len(y))