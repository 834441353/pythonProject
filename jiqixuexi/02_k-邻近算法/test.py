from numpy import *
from sklearn.neighbors import KNeighborsClassifier

def test01():
    fr = open('test.txt')
    linenumber = fr.readlines()
    numberoflines = len(linenumber)
    print("numberofline:%d"%(numberoflines))
    returnMat = zeros((numberoflines,3))#返回给定形状和类型的用0填充的数组
    #return returnMat
    classLabelVector = []

    index = 0
   
    for line in linenumber:
        line = line.strip()
        listFromLine = line.split('\t')
        
  
    return lin
    

def test2():
    for i in range(32):
        print(i)

def test3():
    X = [[0], [1], [2], [3],[4], [5],[6],[7],[8]]
    y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

    neigh = KNeighborsClassifier(n_neighbors=3)  
    neigh.fit(X, y)
    
    print("0.1:%d"%neigh.predict([[0.1]]))
    print("2:%d"%neigh.predict([[2]]))
    print("2.1:%d"%neigh.predict([[2.1]]))
    print("2.9:%d"%neigh.predict([[2.9]]))
    print("3:%d"%neigh.predict([[3]]))
    print("3.1:%d"%neigh.predict([[3.1]]))
    print("5:%d"%neigh.predict([[5]]))
    print("5.1:%d"%neigh.predict([[5.1]]))
    print("5.4:%d"%neigh.predict([[5.4]]))
    print("5.5:%d"%neigh.predict([[5.5]]))
    print("5.51:%d"%neigh.predict([[5.51]]))
    print("5.6:%d"%neigh.predict([[5.6]]))
    print("5.9:%d"%neigh.predict([[5.9]]))
   
