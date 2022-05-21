import pandas as pd
import numpy as np                                             
import matplotlib.pyplot as plt


def estimate_coefficient(x,y):
    N = np.size(x)
    x_mean, y_mean = np.mean(x),np.mean(y)
    
    ss_xy = np.sum(x*y)-N*x_mean*y_mean
    ss_xx = np.sum(x*x)-N*x_mean*x_mean
    
    b1 = ss_xy/ss_xx
    b0 = y_mean - b1*x_mean
    
    return (b0,b1)

def plot_line(x,y,b):
    plt.scatter(x,y, color="m", marker="o",s=30)
    
    y_pred = b[0]+b[1]*x
    
    plt.plot(x,y_pred,color="g")
    plt.show()

def plot_line(x,y,b):
    plt.scatter(x,y, color="m", marker="o",s=30)
    
    y_pred = b[0]+b[1]*x
    
    plt.plot(x,y_pred,color="g")
    plt.show()

x = np.array([10,9,2,15,10,16,11,16])
y = np.array([95,80,10,50,45,98,38,93])
plt.scatter(x,y)
plt.show()


b = estimate_coefficient(x,y)
plot_line(x,y,b)


x = np.array([[10],[9],[2],[15],[10],[16],[11],[16]])
y = np.array([[95],[80],[10],[50],[45],[98],[38],[93]])

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)

plt.plot(x,y,"*")
plt.plot(x,y_pred,color="g")

