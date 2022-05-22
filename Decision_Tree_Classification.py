import pandas as pd
import numpy as np


read_file = pd.read_csv (r'D:\BE Sem 8\LP-3\raw_dataset.txt')
read_file.to_csv (r'D:\BE Sem 8\LP-3\decision_tree_dataset.csv', index=None)

data = pd.read_csv("decision_tree_dataset.csv")

print(data)




x = data.iloc[:,1:-1]
y = data.iloc[:,5].values
print(x)


print(y)








from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()



x=x.apply(LabelEncoder().fit_transform)
print(x)



from sklearn.tree import DecisionTreeClassifier


classifier = DecisionTreeClassifier(criterion="entropy")
classifier.fit(x,y)


inp = np.array([1,1,0,0])
y_pred = classifier.predict([inp])
print(y_pred)


