from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.image as im
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
import cv2
import numpy as np
import pandas as pd
import os
path='F:/dataset1/'
files=os.listdir(path)[:3]
classes={'a':1, 'b':2,'c':3,'d':4}
X=[]
Y=[]
for cl in classes:
    pth=path+'/'+cl #each path is accessed
    print(pth)
    for img_name in os.listdir(pth):
       # print(img_name) #gives the name of each image
      img=cv2.imread(pth+'/'+img_name,0)
      X.append(img)
      Y.append(classes[cl])
print("Data Created")
#print(pd.Series(Y).value_counts())
# Converting From List to Arrays
X=np.array(X)
Y=np.array(Y)



#Reshapping
plt.imshow(X[100],cmap="gray")
#print(X_new.shape)
#print(X_new.ndim)
# ------------ Splitting----------#
xtrain, xtest, ytrain,ytest=train_test_split(X,Y,test_size=0.20, random_state=20)
Xts=xtest
#print(xtrain.shape, ytrain.shape)
#print(xtest.shape, ytest.shape)
#----------Feature Scalling--------------------#
print(xtrain.max())
print(xtest.max())
x_train=xtrain.reshape(len(xtrain),-1)/255
x_test=xtest.reshape(len(xtest),-1)/255
print(x_train.max())
print(x_test.max())
#-----------------Feature Selection ------------------#
print(xtrain.shape, ytrain.shape)
pca=PCA(.98)  # 98% information we need
xtrain=pca.fit_transform(x_train)
xtest=pca.transform(x_test)
print(xtrain.shape, ytrain.shape)
#---------------- Model Training -----------------#
#log=SVC()
#log.fit(xtrain,ytrain)
clf = MLPClassifier(hidden_layer_sizes=(6,5),
                    random_state=5,
                    verbose=True,
                    learning_rate_init=0.01)
clf.fit(xtrain,ytrain)

#-------------- Prediction--------------------#
tr_pred=log.predict(xtrain)
ts_pred=log.predict(xtest)
#------------------ Evalution -----------------#
print("Training Score", accuracy_score(ytrain,tr_pred))
print("Test Score", accuracy_score(ytest,ts_pred))


decode={1:'ALIF', 2:'BEY',3:'JEEM',4:'DAAL'}
for i in range(9):
   plt.subplot(3,3,i+1)
   plt.imshow(Xts[i],cmap='gray')
   plt.title(decode[ts_pred[i]])
   plt.axis('off')
