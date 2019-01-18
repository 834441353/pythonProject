import tkinter as tk
import numpy as np
import os
from PIL import Image, ImageTk
import heapq
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


def pyGUI():
    """
    top = tkinter.Tk()
    li =['MON','THU','WED','THR']
    movie=['APR','FEB','MAR']
    listb =tkinter.Listbox(top)
    listb2=tkinter.Listbox(top)
    buttom = tkinter.Button(top,text='ShowImage')
    text = tkinter.Text(top)
    for item in li:
        listb.insert(0,item)
        
    listb.pack(side=tkinter.LEFT)
    buttom.pack(side=tkinter.LEFT,fill=tkinter.X,anchor=tkinter.NE)
    text.pack(side=tkinter.LEFT)
    top.mainloop()"""
    imgPath = 'Z:\\MenMaskSrc'
    imgList = os.listdir(imgPath)
    images = []
    imagesPath = []

    root = tk.Tk()
    root.title('EX')
    root.geometry('640x480')
    root.resizable(width=False, height=False)
    # l = tk.Label(root,text = 'Color',bg = 'green',font =('Arial',12), width = 20,height=2)

    for imgName in imgList:
        if '.npy' in imgName:
            continue
        imgAbsPath = os.path.join(imgPath, imgName)
        # print(imgAbsPath)
        # img = misc.imread(imgAbsPath, 'L')
        img_open = Image.open(imgAbsPath)

        img = ImageTk.PhotoImage(img_open)

        if img is None:
            continue
        images.append(img)
        imagesPath.append(imgAbsPath)

    # bm = tk.PhotoImage(file = "D:\\TestImg\\1591928_021sf.png")
    l = tk.Label(root, image=images[1])
    l.pack(side=tk.TOP)
    # t = tk.Text(root,width=100,height=10,fg='red')
    # t.pack(side = tk.TOP)

    t = tk.Listbox(root)
    t.pack(side=tk.TOP)

    idxVar = tk.StringVar()
    idxVar.set(0)

    def PRE():
        # idx = random.randint(0,len(images) - 1)
        idx = (int)(idxVar.get())
        idx = idx + 1
        if idx > len(images) - 1:
            idx = len(images) - 1
        idxVar.set(idx)
        l.configure(image=images[idx])
        # t.delete(1.0,2.0)
        t.insert(tk.END, imagesPath[idx] + '\n')

    def POST():
        # idx = random.randint(0,len(images) - 1)
        idx = (int)(idxVar.get())
        idx = idx - 1
        if idx < 0:
            idx = 0
        idxVar.set(idx)
        l.configure(image=images[idx])
        # t.delete(1.0,2.0)
        t.insert(tk.END, imagesPath[idx] + '\n')

    var = tk.StringVar()
    var.set(0)

    def insert():
        num = np.random.randint(0, 100)
        # var.set(10)
        num = (int)(var.get())
        t.insert(tk.END, "tkInter-----%d\n" % (num))

    def delete():
        t.delete(0, tk.END)

    r1 = tk.Radiobutton(root, text='未选中', value='A', command=insert)
    r1.pack()
    c = tk.Checkbutton(root, text='选中', variable=var, command=insert)  # variable用来表示按钮的状态（是否被按下）
    c.pack()

    tk.Button(root, text="DEL", command=delete).pack(side=tk.LEFT)
    tk.Button(root, text="POST", command=POST).pack(side=tk.RIGHT)
    tk.Button(root, text="PRE", command=PRE).pack(side=tk.LEFT)
    root.mainloop()


def computeFeatureSimilar(feature0, feature1):
    feature0Size = feature0.shape
    feature1Size = feature1.shape

    # print(feature0Size)
    meanA = []
    # for idx in range(0,feature0Size[0],1):
    for idx in range(0, feature0Size[0]):
        baseFeature = feature0[idx]
        mean = np.mean(np.linalg.norm(feature1 - baseFeature, axis=1))
        meanA.append(mean)

    if len(meanA) == 0:
        return -1
    avg = np.mean(np.array(meanA))
    return avg


class ImageProcess:
    def __init__(self, root):
        # self.monty = tk.LabelFrame(root, text=" Monty Python ")
        # self.monty.grid(column=0, row=0, padx=10, pady=10)

        # self.bm0 = tk.PhotoImage(file = "D:\\TestImg\\1591928_021sf.png")
        # self.lb0 = tk.Label(root,image = self.bm0)
        # self.lb0.grid(row = 0,column = 0)

        # self.bm1 = tk.PhotoImage(file = "D:\\TestImg\\1591928_021sf.png")
        # self.lb1 = tk.Label(root,image = self.bm1)
        # self.lb1.grid(row = 0,column = 1)

        self.lb0 = ttk.Label(root, text='Image Path')
        self.lb0.grid(row=0, column=0)

        self.name = tk.StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
        self.entry = ttk.Entry(root, width=50,
                               textvariable=self.name)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
        self.entry.grid(row=0, column=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
        self.entry.focus()

        self.bt0 = ttk.Button(root, text="Load", command=self.loadImage)
        self.bt0.grid(row=0, column=2)

        self.bt1 = ttk.Button(root, text="Next", command=self.nextImage)
        self.bt1.grid(row=0, column=3)

        self.bt2 = ttk.Button(root, text="Save", command=self.saveImage)
        self.bt2.grid(row=0, column=4)

        self.labelFrame = tk.LabelFrame(root, text='IMG', padx=5, pady=5)
        self.labelFrame.grid(row=1, column=0, columnspan=5)

        self.width = 160
        self.height = 160

        self.images = []
        self.imagesPath = []

        self.peopleArray = []
        self.featureArray = []

        self.ckbArray = []
        self.ckbVarArray = []
        self.labelArray = []
        # self.btArray = []

        self.curSinglePeopleCluster = []
        self.haveBeenSavedIdx = []

        # img_open = Image.open('D:\\TestImg\\040395_1-FaceId-0_right_A0_idx10.jpg')
        img_open = Image.new("RGB", (self.width, self.height), "gray")
        self.img = ImageTk.PhotoImage(img_open)

        idx = 0
        for r in range(1, 9, 2):
            for c in range(5):
                self.images.append(self.img)
                label = ttk.Label(self.labelFrame, image=self.img)
                self.labelArray.append(label)
                self.labelArray[idx].grid(row=r, column=c)

                ckBVar = tk.IntVar()
                ckb = ttk.Checkbutton(self.labelFrame, text='%d' % (idx), variable=ckBVar)
                self.ckbVarArray.append(ckBVar)
                self.ckbArray.append(ckb)
                self.ckbArray[idx].grid(row=r + 1, column=c)

                idx = idx + 1

        self.peopleIdx = 0

    def loadImage(self):
        # featureBasePath = 'S:\\ClusterFaceData'
        if len(self.peopleArray) != 0:
            messagebox.showinfo(title='X', message='Images have been loaded!')
            return
        featureBasePath = self.entry.get()
        if os.path.exists(featureBasePath):
            peopleIDList = os.listdir(featureBasePath)
            for people in peopleIDList:
                path = os.path.join(featureBasePath, people + '\\feature.npy')

                if os.path.exists(path):
                    feature = np.load(path)
                    imgPath = os.path.join(featureBasePath, people)
                    imgList = os.listdir(imgPath)
                    imgListNew = [os.path.join(imgPath, v) for v in imgList if '.jpg' in v]
                    self.peopleArray.append(imgListNew)
                    self.featureArray.append(feature)
                    self.haveBeenSavedIdx.append(0)
        else:
            messagebox.showinfo(title='X', message='Invalid image path!')

        # print(imgPath)
        """
        if os.path.exists(imgPath):
            #imgPath = 'Z:\\MenMaskSrc'
            imgList = os.listdir(imgPath)
            #print(imgList)
            for imgName in imgList:
                if '.bmp' in imgName:
                    imgAbsPath = os.path.join(imgPath,imgName)
                    print(imgAbsPath)
                    #img = misc.imread(imgAbsPath, 'L')
                    img_open = Image.open(imgAbsPath)

                    img=ImageTk.PhotoImage(img_open)
                    
                    if img is None:
                        continue  
                    self.images.append(img)
                    self.imagesPath.append(imgAbsPath)
        else:
            print('No Dir')"""

    def nextImage(self):
        for var in self.ckbVarArray:
            var.set(0)
        print('People Idx %d' % (self.peopleIdx))

        peopleNum = len(self.peopleArray)
        if peopleNum == 0:
            messagebox.showinfo(title='X', message='No image data')
            return

        if self.peopleIdx == peopleNum:
            messagebox.showinfo(title='X', message='END')
            return

        while self.haveBeenSavedIdx[self.peopleIdx] == 1:
            self.peopleIdx = self.peopleIdx + 1
            if self.peopleIdx == peopleNum:
                messagebox.showinfo(title='X', message='END')
                return

        # if self.peopleIdx >= peopleNum:
        #    self.peopleIdx = 0
        self.curSinglePeopleCluster = []
        feature0 = self.featureArray[self.peopleIdx]
        # print(idx)
        similarScore = []
        for jdx in range(peopleNum):  # 0==>start  end==>num
            # print('jdx',jdx)
            feature1 = self.featureArray[jdx]
            score = computeFeatureSimilar(feature0, feature1)
            similarScore.append(score)
            # print(score)
        # break
        # max_num_index_list = list(map(similarScore.index, heapq.nlargest(10, similarScore)))
        min_num_index_list = list(map(similarScore.index, heapq.nsmallest(10, similarScore)))
        # print(min_num_index_list)
        for k, minIdx in enumerate(min_num_index_list):
            # print(self.peopleArray[minIdx],similarScore[minIdx])
            # print(self.peopleArray[minIdx][0])
            num = np.random.randint(0, len(self.peopleArray[minIdx]))
            img_open = Image.open(self.peopleArray[minIdx][num])
            self.images[k] = ImageTk.PhotoImage(img_open.resize((self.width, self.height)))
            self.labelArray[k].configure(image=self.images[k])
            self.curSinglePeopleCluster.append(minIdx)
        self.peopleIdx = self.peopleIdx + 1

        # num = np.random.randint(0,10)
        # img_open = Image.open(self.peopleArray[0][num])
        # self.images[0] =ImageTk.PhotoImage(img_open.resize((self.width,self.height)))
        # self.labelArray[0].configure(image = self.images[0])
        # featureBasePath = 'S:\\ClusterFaceData'
        # return

    def saveImage(self):
        if len(self.peopleArray) == 0:
            messagebox.showinfo(title='X', message='No image data')
            return

        # print((int)(self.ckbVarArray[0].get()))
        print('----------SAVE IMAGE---------------')
        saveTotalNum = 0
        savePeoplePathArray = []
        for k, minIdx in enumerate(self.curSinglePeopleCluster):
            if (int)(self.ckbVarArray[k].get()) == 1:

                if self.haveBeenSavedIdx[minIdx] == 0:
                    self.haveBeenSavedIdx[minIdx] = 1
                else:
                    messagebox.showinfo(title='X', message='Have been saved')
                    return
                print(k, self.peopleArray[minIdx][0])
                savePeoplePathArray.append(self.peopleArray[minIdx][0])
                saveTotalNum = saveTotalNum + 1
        if saveTotalNum == 0:
            messagebox.showinfo(title='X', message='No Save data')
        else:
            fileTimeName = datetime.strftime(datetime.now(), '%Y%m%d-%H%M%S')
            with open('%s.txt' % (fileTimeName), 'w') as f:
                for path in savePeoplePathArray:
                    f.write('%s\n' % (path))

    def insert(self):
        num = np.random.randint(0, 100)
        # self.listbox0.insert(tk.END, "tkInter-----%d\n"%(num))


if __name__ == "__main__":
    # pyGUI()
    root = tk.Tk()
    root.title('EX')
    root.geometry('850x850')
    root.resizable(width=False, height=False)
    ImageProcess(root)
    root.mainloop()
