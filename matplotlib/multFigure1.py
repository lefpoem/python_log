import matplotlib.pyplot as plt
# generate the first figure
plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3,4])
plt.subplot(212)
plt.plot([3,4,5,6])

# generate the second figure
plt.figure(2)
plt.scatter([0,1,2,3],[3,4,5,6])

# update the attribute of the first figure
plt.figure(1)
plt.subplot(211)
plt.title('Demo')

plt.show()