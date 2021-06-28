import numpy as np
import matplotlib.pyplot as plt

data = {
    # the deafult sample from[0,50)
    'a' : np.arange(50),
    # generate random integar from[0,50) and size is 50
    'c' : np.random.randint(0,50,50),
    # generate one-by-50 array from standard normal distribution
    'd' : np.random.randn(50)
}
data['b'] = data['a'] + 10*np.random.randn(50)
data['d'] = np.abs(data['d'])*100
# scatter(x,y,color,size,data)
plt.scatter('a','b',c='c',s='d',data=data)
plt.show()