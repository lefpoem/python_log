import matplotlib.pyplot as plt
import numpy as np
def f(t):
    return (1/(np.sqrt(2*np.pi)))*np.exp(-(1/2)*t**2)
m = np.random.randn(1000)
plt.plot(m,f(m))
plt.show()