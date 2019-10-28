import numpy as np


class AdalineGD(object):
    """
    Parameters
    --------------
    eta0 : learning rate
    n_iter : iteration on data set

    Attributes
    ---------------
    w_ : 1d weight array
    error_ : error list
    """

    def __init__(self,eta0,n_iter):
        self.eta0=eta0
        self.n_iter=n_iter
        self.w_ = []


    def fit(self,data_matrix,class_labels_vector):
        """
            Define attributes
            """
        self.w_ = np.zeros(1 + data_matrix.shape[1])
        self.error_ : []
        self.cost_vector = list()

        for i in range(self.n_iter):
            result_vector = self.matrix_to_weight_vector_dot_product(data_matrix)
            error_vector = class_labels_vector - result_vector

            self.w_[1:] += self.eta0 * (np.dot(data_matrix.T,error_vector))
            self.w_[0] += self.eta0 * error_vector.sum()
            self.cost_vector.append(sum(np.square(error_vector))/2)


    def matrix_to_weight_vector_dot_product(self,data_matrix):
        return np.dot(data_matrix,self.w_[1:])+self.w_[0]

    def activation(self,test_data_matrix):
        return self.matrix_to_weight_vector_dot_product(test_data_matrix)

    def predict(self,test_data_matrix):
        return np.where(self.activation(test_data_matrix) >=0.0,1,-1)

    def plot(self):
        import matplotlib.pyplot as plt
        plt.scatter(range(1,len(self.cost_vector)+1),self.cost_vector,marker='o')
        plt.show()


class PreProcessing(object):

    def __init__(self):

        pass

    def set_data(self,data,target):
        self.data=data
        self.target=target
        return self

    def get_train_test_splits(self):
        import sklearn.model_selection as ms
        return  ms.train_test_split(self.data,self.target,random_state=1,shuffle=True,train_size=0.7)


def main():
    import sklearn.datasets as data
    iris = data.load_iris()

    p = PreProcessing()
    training_data,test_data,training_target,test_target = p.set_data(iris.data,iris.target).get_train_test_splits()
    print(test_data)
    print(test_target)
    # model = AdalineGD(0.001,60)
    # # print(iris.data[:10,:])
    # # print(np.array(iris.target[0:10])[np.newaxis])
    # data =np.concatenate((iris.data[:6,:],iris.data[145:,:]))
    # target = np.concatenate((iris.target[0:6],iris.target[145:]))
    #
    # print(data.shape)
    # print(target.shape)
    # model.fit(data,target)
    # model.plot()

if __name__ == '__main__':
    main()