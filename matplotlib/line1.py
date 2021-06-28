# import plot kit from matplotlib 
import matplotlib.pyplot as plt

# input a sequence of y values
line = plt.plot([1,2,3,4])

# input the label of y
plt.ylabel('some numbers')
'''Since python ranges start with 0,
the defualt x vector has the same length
as y but start with 0.Hence the x data are [0,1,2,3]'''
plt.setp(line) #set priority
antialiased : False
plt.grid(True)
plt.show()