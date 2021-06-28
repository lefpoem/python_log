'''Ploting several lines with different format style
in one fuction call numpy arrays'''
import numpy as np
import matplotlib.pyplot as plt
# evenly sampled time at 200ms interval from [0,5)
t = np.arange(0.,5.,0.2)
# plot with red dashes,blue square and green triangle
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()