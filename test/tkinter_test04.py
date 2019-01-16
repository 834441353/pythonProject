import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

from PIL import Image, ImageTk
import queue


class App(tk.Frame):
    def __init__(self, root):
        self.lb0 = ttk.Label(root, text='File Name:')
        self.lb0.grid(row=0, column=0)

        self.onename = tk.StringVar(root)
        self.textbox = ttk.Entry(root, width=50, textvariable=self.onename)
        self.textbox.grid(row=0, column=1)
        self.textbox.focus()

        self.but01 = ttk.Button(root, text='loadFile', command=self.loadfile)
        self.but01.grid(row=1, column=0)
        self.butbuff = 0
        self.width = 224
        self.height = 224
        self.labelarr = []

    def loadfile(self):
        self.butbuff = 0
        path = self.onename.get()
        print(path)
        if not os.path.exists(path):
            self.mywaringmessaeg('请输入有效文件路径')
        elif os.path.isfile(path):
            file = open(path)
            filecontent = file.readlines()
            file.close()
            self.tp = tk.Toplevel()
            self.loadimg0(self.tp, filecontent)
        elif os.path.isdir(path):
            self.dirlist = os.listdir(path)
            self.dirlen = len(self.dirlist)

            self.tp = tk.Toplevel()

            # 第一个文件被打开
            self.previousbut = ttk.Button(self.tp, text='previous')
            self.previousbut.configure(command=self.previousbut_click)
            self.previousbut.configure(state='disable')
            self.previousbut.grid(row=0, column=0)

            self.nowfile = ttk.Label(self.tp, text=self.dirlist[0], width=50)
            self.nowfile.grid(row=0, column=1)

            self.nextbut = ttk.Button(self.tp, text='next', state='disable')
            if self.dirlen != 1:
                self.nextbut.configure(state='able')
                self.nextbut.configure(command=self.nextbut_click)
            self.nextbut.grid(row=0, column=2)

            self.imgLabel = ttk.LabelFrame(self.tp, text='img')
            self.imgLabel.grid(row=1, column=0, columnspan=5)

            self.labelarr = []
            img_open = Image.new("RGB", (self.width, self.height), "gray")
            self.img = ImageTk.PhotoImage(img_open)
            a = 0
            for i in range(4):
                for j in range(5):
                    label = ttk.Label(self.imgLabel, image=self.img)
                    self.labelarr.append(label)
                    self.labelarr[a].grid(row=i, column=j)
                    a += 1
            print(self.dirlist[0])
            file = open(os.path.join(self.onename.get(), self.dirlist[0]))
            imgarr = file.readlines()
            file.close()
            self.loadimg(imgarr)

    def previousbut_click(self):
        self.butbuff -= 1
        self.nowfile['text'] = self.dirlist[self.butbuff]
        file = open(os.path.join(self.onename.get(), self.dirlist[self.butbuff]))
        imgarr = file.readlines()
        file.close()
        self.loadimg(imgarr)
        self.nextbut.configure(state='able')
        if self.butbuff == 0:
            self.previousbut['state'] = 'disable'
            return

    def nextbut_click(self):

        self.butbuff += 1
        self.nowfile['text'] = self.dirlist[self.butbuff]
        file = open(os.path.join(self.onename.get(), self.dirlist[self.butbuff]))
        imgarr = file.readlines()
        file.close()
        self.loadimg(imgarr)
        self.previousbut.configure(state='able')
        if self.butbuff + 1 == self.dirlen:
            self.nextbut['state'] = 'disable'
            return

    def mywaringmessaeg(self, message):
        messagebox.showwarning('Python Message Warning Box', message)

    def loadimg(self, imgarr):
        for i in range(20):
            self.labelarr[i]['image'] = self.img
        self.imgpath = []

        # imgarr = [
        #     'S:\ClusterFaceData\datahome_zhaji_20181204_室外_15-111_51_\datahome_zhaji_20181204_室外_15-111_51_gray_503.jpg']
        arrlen = len(imgarr)
        print(imgarr)
        for i in range(arrlen):
            print(imgarr[i].strip())
            if not os.path.exists(imgarr[i].strip()):
                continue
            img = Image.open(imgarr[i].strip())
            imga = ImageTk.PhotoImage(img)
            self.imgpath.append(imga)
            self.labelarr[i]['image'] = self.imgpath[i]
            self.labelarr[i].bind("<Button-1>", self.handlerAdaptor(self.pathwrite, a=imgarr[i].strip()))

    def loadimg0(self, master, imgarr):

        self.imgpath = []
        self.labelarr = []
        row = 0
        col = 0

        # imgarr = [
        #     'S:\ClusterFaceData\datahome_zhaji_20181204_室外_15-111_51_\datahome_zhaji_20181204_室外_15-111_51_gray_503.jpg']
        arrlen = len(imgarr)
        print(imgarr)
        for i in range(arrlen):

            print(imgarr[i].strip())
            if not os.path.exists(imgarr[i].strip()):
                continue
            img = Image.open(imgarr[i].strip())
            imga = ImageTk.PhotoImage(img)
            self.imgpath.append(imga)
            label = ttk.Label(master)
            self.labelarr.append(label)
            self.labelarr[i]['image'] = self.imgpath[i]
            if i % 5 == 0:
                row += 1
                col = 0
            self.labelarr[i].grid(row=row, column=col)
            self.labelarr[i].bind("<Button-1>", self.handlerAdaptor(self.pathwrite, a=imgarr[i].strip()))
            col += 1

    def handlerAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def pathwrite(self, event, a):
        print('del' + str(a))
        if os.path.isfile(self.onename.get()):
            filename = './txt/' + self.onename.get().split('/')[-1].split('.')[0] + '_.txt'
        else:
            filename = './txt/' + self.dirlist[self.butbuff].split('.')[0] + '_.txt'
        file = open(filename, 'a')
        file.write(str(a) + '\n')
        file.close()


if __name__ == '__main__':
    root = tk.Tk()

    root.title('EX')
    # root.geometry('850x850')
    root.resizable(width=False, height=False)  # 是否允许改变大小
    App(root)
    root.mainloop()
