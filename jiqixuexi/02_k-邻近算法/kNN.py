from numpy import *
import operator
import os

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


def classify0(inX,dataSet,labels,k):
    
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    #sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)#排序
    return sortedClassCount[0][0]

def file2matrix(filename):
    #打开文件
    fr = open(filename)
    arrayOLines = fr.readlines() #读取所有行，返回列表
    numberOfLines = len(arrayOLines)#返回对象长度或者是项目个数
    returnMat = zeros((numberOfLines,3))  #返回一个给定形状和类型的用0填充的数组   创建返回的NumPy矩阵
    classLabelVector = []
    index = 0
    #解析文件数据到列表
    for line in arrayOLines:
        line = line.strip()#移除字符串头尾指定的字符
        listFromLine = line.split('\t')#以制表符分割字符串
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector


##############################################手写识别#######################################################
'''将图像转化为向量：该函数创建1x1024的NumPy数组，然后打开给指定文件，循环独
处文件的前32行，并将每行的头32个字符储存在NumPy数组中，最后返回数组
'''
def img2vector(filename):
    returnVect = zeros((1,1024))#创建一个空数组
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels = []

    #获取目录内容
    trainingFileList = os.listdir('./digits/trainingDigits/')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('./digits/trainingDigits/%s'%fileNameStr)
    testFileList = os.listdir('./digits/testDigits/')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('./digits/testDigits/%s'%fileNameStr)
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print("the classifier came back with:%d ,the real answer is:%d" % (classifierResult,classNumStr))

        if (classifierResult != classNumStr):
            errorCount +=1.0
    print("\nthe total number of error is: %d"%errorCount)
    print("\nthe total error rate is: %f"%(errorCount/float(mTest)))



    
'''
if __name__ == '__main__':
    testVector = img2Vector('digits/testDigits/0_13.txt')
    print(testVector)
'''