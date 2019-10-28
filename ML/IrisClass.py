import sklearn.datasets as data


def main():
    iris=data.load_iris()
    print(iris.items())
    # print(iris.data[:])
    # print(iris.data[:,0])
    # print(iris.data[:, 1])

if __name__ == '__main__':
    main()
