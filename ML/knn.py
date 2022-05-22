import pandas as pd
import numpy as np

dataset = {'x':[2,4,4,4,6,6],
           'y':[4,4,6,2,4,2],
           'res':['negative','positive','negative','negative','negative','positive']}


print(dataset)

dataset = pd.DataFrame(dataset,columns=["x","y","res"])

print(dataset)

X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,2].values

#import KNeighborshood Classifier and create object of it
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,y)

#predict the class for the point(6,6)
X_test=np.array([6,2])
y_pred=classifier.predict([X_test])
print ('General KNN:',y_pred)

classifier=KNeighborsClassifier(n_neighbors=3,weights='distance')
classifier.fit(X,y)

#predict the class for the point(6,6)
X_test=np.array([6,2])
y_pred=classifier.predict([X_test])
print ('Distance Weighted KNN:',y_pred)