import numpy as np
import matplotlib.pyplot as plt
# set random start point
np.random.seed(19680801)

# mean=loc,std devation=scale,amount=1000
y = np.random.normal(loc=0.5,scale=0.4,size=1000)

# limit y to the range(0,1)
y = y[(y>0) & (y<1)]
y.sort()

# generate a one-by-len array
x = np.arange(len(y))

# generate a linear y
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# generate a log y
plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# generate a symlog y
plt.subplot(223)
plt.plot(x,y-y.mean())
# linthresh is threshold
plt.yscale('symlog',linthresh=0.01)
plt.title('symlog')
plt.grid(True)

#generate a logit y
plt.subplot(224)
plt.plot(x,y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

#Since logit take some space,adjustment is needed.
plt.subplots_adjust(top=0.85,bottom=0.1,right=0.9,left=0.3,hspace=0.35,wspace=0.35)
plt.show()