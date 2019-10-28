import matplotlib.pyplot as plt
import sklearn.datasets as data
import numpy as np
import pandas as pd
import re
import sklearn.linear_model as lm

import sklearn.model_selection as ms

pd.set_option('display.max_columns',None)
pd.set_option('display.width',200)

class Iris(object):

    df : pd.DataFrame



    def __init__(self,eta0=0.01):
        self.iris=data.load_iris()
        self.train_data=[]
        self.train_target=[]
        self.test_data=[]
        self.test_target=[]
        self.model=lm.Perceptron(eta0=eta0,random_state=1,max_iter=1000)

    # @staticmethod
    # def replace_junk(x):
    #     return re.sub("[()]","",(re.sub("[\s]+","_",x)))

    replace_junk=lambda x:re.sub("[()]","",(re.sub("[\s]+","_",x)))

    def get_dataframe_object(self):
        columns=self.iris.feature_names +['targetType']
        df=pd.DataFrame(data=np.c_[self.iris.data,self.iris.target]
                        ,columns=list(map(lambda x: Iris.replace_junk(x),columns)))

        # return df.where(df['targetType'] <1,inplace=False).dropna()
        # columns = self.iris.feature_names
        # return list(map(lambda x: Iris.replace_junk(x),columns))
        # return list(map(lambda x: Iris.replace_junk(x), columns))
        return df

    def chart_plot(self,x_index,y_index):

        # this formatter will label the colorbar with the correct target names
        formatter = plt.FuncFormatter(lambda i, args: self.iris.target_names[int(i)])

        plt.figure(figsize=(5, 4))
        plt.scatter(self.iris.data[:, x_index], self.iris.data[:, y_index], c=self.iris.target)
        plt.colorbar(ticks=[0, 1, 2], format=formatter)
        plt.xlabel(self.iris.feature_names[x_index])
        plt.ylabel(self.iris.feature_names[y_index])

        plt.tight_layout()
        plt.show()

    def train_test_split(self):
        import sklearn.model_selection as ms
        df=self.get_dataframe_object()
        # self.train_data,self.test_data,self.train_target,self.test_target=\
        #     ms.train_test_split(self.iris.data,self.iris.target,shuffle=True,train_size=0.8)
        self.train_data,self.test_data,self.train_target,self.test_target=\
            ms.train_test_split(df.iloc[:,0:4],df.iloc[:,4],shuffle=True)

        # print(self.train_data)
        # print(self.train_target)

    def train_test_model(self):
        self.model.fit(self.train_data,self.train_target)

    def validate_model_results(self):
        predicted_target=self.model.predict(self.test_data)

        import sklearn.metrics as mt
        result=mt.accuracy_score(self.test_target,predicted_target)
        print("result = ",result*100)

def main():

    # The indices of the features that we are plotting
    x_index = 0
    y_index = 1

    #chart_plot(2,3)
    i=Iris(0.0001)
    # print(i.get_dataframe_object())
    i.train_test_split()
    for x in range(10):
        i.train_test_model()

    i.validate_model_results()


if __name__ == '__main__':
    main()
