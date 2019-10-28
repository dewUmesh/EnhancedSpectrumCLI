import numpy as np
import matplotlib.pyplot as plt
"""
1. Import iris data set from sklearn dataset module
"""
import sklearn.datasets as dt
iris=dt.load_iris()
print(iris.data)
print(iris.target)
plt.scatter(iris.data,iris.target)
plt.show()

"""
2. Verify the features sepal length,sepal width,petal length,petal width
   verify classes setosa,vercicolor and verginica are [0,1,2] 
"""

"""
3. Split dataset in train_test_split
    using sklearn 
"""

"""
4. Apply standard scaler on features and target class for train and test dataset
    fit and apply transform
"""

"""
5. create cross validation object for features of train data set using kfold
"""

"""
6. Create model object and apply fit to standardized/normalized data
"""

"""
7. Model validation and acuracy score calculation from matrics module
"""

