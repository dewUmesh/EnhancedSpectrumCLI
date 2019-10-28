import numpy as np
def main():

    #
    # a=[1,2]
    # b=[3,4]
    #
    # # result =
    #
    # print(np.dot(a,b))
    # print(zip(a,b))
    # for i in zip(a,b):
    #     print(i)

    import sklearn.datasets as dt
    iris=dt.load_iris()
    x=iris.data[:2,:]
    x=np.array([[1,1,1,1],[2,2,2,2]])
    print(x)

    y=iris.target[:2]

    y[0]=1
    y[1]=2
    print(y)
    print(x.shape)
    global weight_;
    weight_=np.zeros(1+x.shape[1])

    # print(weight_)
    # weight_[1:] += 1
    print(weight_)
    print("-----------------")
    for xi,target in zip(x,y):
        print(xi)
        print(target)
        
        update=target - predict(x)
        # weight_[1:]+=update*xi
        # weight_[0]+=update
        print("=============")
        print(weight_)


def predict(x):
    print("where condition : ")
    print(np.where(net_input(x) >=0.0,1,-1))
    return np.where(net_input(x) >=0.0,1,-1)

def net_input(x):
    print("dot product : ")
    print(np.dot(x,weight_[1:]))
    return np.dot(x,weight_[1:])

if __name__ == '__main__':
    main()