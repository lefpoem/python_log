import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
from matplotlib import font_manager

# generate a coordinate matrices
xx,yy = np.meshgrid(np.linspace(-5,5,500),np.linspace(-5,5,500),sparse=False)
#generate 200 training set ,2 dimensions
X = 0.3*np.random.randn(100,2)
X_train = np.r_[X+2,X-2] # e.g. r_ catenate [1,2,3] and [4,5,6] to [1,2,3,4,5,6]

# genetate 40 regular novel observation
X = 0.3*np.random.randn(20,2)
X_test = np.r_[X+2,X-2]

# generate 20 abnormal novel observation
X_outliers = np.random.uniform(low=-4,high=4,size=(20,2))

# fit the model
clf = OneClassSVM(nu=0.1,gamma=0.1,kernel='poly')
clf.fit(X_train)

# predict observation
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_errors_train = y_pred_train[y_pred_train == -1].size
n_errors_test = y_pred_test[y_pred_test == -1].size # size() is int object
n_errors_outliers = y_pred_outliers[y_pred_outliers == -1].size

# calculate distance,ravel扁平化处理，C——连接
Z = clf.decision_function(np.c_[xx.ravel(),yy.ravel()])# 250000
Z = Z.reshape(xx.shape) # 500by500

# contour and filled contour:draw contour
plt.title('Novelty Detection')
plt.contourf(xx,yy,Z,levels=np.linspace(Z.min(),0,7),cmap=plt.cm.PuBu)
a = plt.contour(xx,yy,Z,levels=[0],linewidths=2,colors='darkred')
plt.contourf(xx,yy,Z,levels=[0,Z.max()],colors='palevioletred')

# indicted train, test,oulies points
b1 = plt.scatter(X_train[:,0],X_train[:,1],c='white',s=40,edgecolors='k')
b2 = plt.scatter(X_test[:,0],X_test[:,1],c='blueviolet',s=40,edgecolors='k')
c = plt.scatter(X_outliers[:,0],X_outliers[:,1],c='gold',s=40,edgecolors='k')

# auto scale so that show all data
plt.axis('tight')
plt.xlim(-5,5)
plt.ylim(-5,5)

# set a legend to illustrate plot
plt.legend([a.collections[0],b1,b2,c],["learning frontier","training observations",
"new ragular observations","new abnormal observations"],loc="upper left",
prop=font_manager.FontProperties(size=11))

# set xlabel;xlaber param is 3
plt.xlabel("errors train:%d/200;errors_test:%d/40" "errors_outliers:%d/20"
% (n_errors_train,n_errors_test,n_errors_outliers))

plt.show()
