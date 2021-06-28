import numpy as np
import matplotlib.pyplot as plt

# set text at a arbitary point
mu,sigma = 100,15
# set one novel normal distribution at mu and sigma
x = mu + sigma*np.random.randn(10000)

# the histogram of data
# x array 1 by 100,rwidth:relative width
n,bins,patches = plt.hist(x,50,density=1,facecolor='g',alpha=1,rwidth=0.5)

# set grid
plt.grid(True)

# label and title
plt.xlabel('Smarts')
plt.ylabel('Probality')
plt.title('Histogram of IQ')

# insert text at the unique postition
plt.text(60,.025,r'$\mu=100, \ \sigma=15$') # shows that allow latek

plt.annotate('local',xy=(50,0.01),xytext=(60,0.020),arrowprops=dict(facecolor='black', shrink=0.05))

# set a range about x and y axes
plt.axes([40,160,0,0.03])
plt.show()