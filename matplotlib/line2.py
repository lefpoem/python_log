import matplotlib.pyplot as plt

#To plot x versus y,u can write
plt.plot([1,2,3,4],[1,4,9,16],'ro') # 'ro' indicates red pie

#indicate x ranges 0 to 6 and y ranges 0 to 20
#axis[xmin,xmax,ymin,ymax]
plt.axis([0,6,0,20])
plt.show()