import pandas as pd
import numpy as np


read_file = pd.read_csv (r'raw_dataset.txt')
read_file.to_csv (r'decision_tree_dataset.csv', index=None)

data = pd.read_csv("decision_tree_dataset.csv")
print('--------------------------- Printing the data ---------------------------')
print(data)
print()


print('--------------------------- values in x ---------------------------')
x = data.iloc[:,1:-1]
y = data.iloc[:,5].values
print(x)
print()
print('--------------------------- values in y ---------------------------')
print(y)
print()


print('--------------------------- Label Encoder ---------------------------')




from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

print('--------------------------- Label Encoder on the values of x ---------------------------')

x=x.apply(LabelEncoder().fit_transform)
print(x)
print()

print('--------------------------- Sklearn - Decision Tree Classifier ---------------------------')
from sklearn.tree import DecisionTreeClassifier


classifier = DecisionTreeClassifier(criterion="entropy")
classifier.fit(x,y)


inp = np.array([1,1,0,0])
y_pred = classifier.predict([inp])
print(y_pred)


