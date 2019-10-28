import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 =pd.read_csv('iris.csv')
df=pd.DataFrame(df1)
print(df)
x=df.iloc[:6,[0,1]].values
print(x)
# y=df.iloc[0:2,2:]
# print(y)
print("---------------------")
y=df.iloc[:6,[2]].values
print(y)
y=np.where(y=='setosa',1,-1)


print(y)
print("---------------")
# plt.scatter(x[:3,0],x[:3,1],c='red',marker='o',label='verginica')
# plt.scatter(x[3:6,0],x[3:6,1],c='green',marker='o',label='setosa')
# plt.show()

weight=np.zeros(x.shape[1])
print(weight)
eta=0.1
error_ :list
error_=[]

def predict(xi):
    t=np.where( dotproduct(xi) >= 0, 1, -1)
    return t

def dotproduct(xi):
    p=np.dot(xi, weight)
    return p

for _ in range(2):
    print("====================================== ", _)
    error=0
    for xi ,target in zip(x,y):

        #print(weight, xi , y)
        pr=predict(xi)
        update=(target - pr)
        weight += update * xi
        print(weight,xi,target,update)
        if (update != 0.0):
            error += 1

    error_.append(error)

print("Error per run ")
print(error_)




