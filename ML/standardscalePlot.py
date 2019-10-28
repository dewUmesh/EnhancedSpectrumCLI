from matplotlib import pyplot as plt
import numpy as np
import scipy.stats
import math
import pandas as pd

# data=[[2,1,3],[20,10,30],[200,100,300],[2000,1000,3000]]
# x1=np.random.normal(0,2,10)
# x2=np.random.normal(5,3,10)
# x3= np.random.normal(-5,5,10)
# data={'a':x1,'b':x2,'c':x3}
# # print(data)
# df=pd.DataFrame(data,columns=['a','b','c'])
# print(df)
# df.plot(kind='kde')
# plt.plot(df)
# plt.show()

# x=[-5,-4,-2,-1,0,1,2,4,5]
# y= - np.square(x)
# plt.plot(data)
# plt.show()

s = np.random.chisquare(8,100)
plt.plot(s)
plt.show()