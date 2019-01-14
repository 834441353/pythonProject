import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

from PIL import Image, ImageTk
import queue


class App(tk.Frame):
    def __init__(self, root):
        self.lb0 = tk.Label(root, text='File Name:')
        self.lb0.grid(row=0, column=0)

        self.name = tk.StringVar(root)
        self.textbox = tk.Entry(root, width=50, textvariable=self.name)
        self.textbox.grid(row=0, column=1)

        self.but01 = ttk.Button(root, text='loadfile', command=self.loadfile)
        self.but01.grid(row=1, column=0)

        self.imgpath = []

        self.labelarr = []
        # self.lbf = ttk.LabelFrame(root, text='img',padx=5, pady=5 )
        # root.mainloop()

    def but01_click(self):
        # messagebox.showinfo('Python Message Info Box', self.name.get())
        self.tp = tk.Toplevel()
        self.tp.title = 'a'
        self.but01_tp = ttk.Button(self.tp, text='a', command=self.but01_click)
        self.but01_tp.grid(row=0, column=0)

    def loadfile(self):
        path = self.name.get()
        if not os.path.exists(path):
            self.mywaringmessaeg('请输入有效文件路径')
        else:
            # print('a')
            file = open(path)
            # print(file.readlines())
            a = file.readlines()
            file.close()
            self.loadimg(a)

    def mywaringmessaeg(self, message):
        messagebox.showwarning('Python Message Warning Box', message)

    def loadimg(self, imgarr):
        self.tp = tk.Toplevel()
        self.imgpath = []
        self.labelarr = []
        # imgarr = [
        #     'S:\ClusterFaceData\datahome_zhaji_20181204_室外_15-111_51_\datahome_zhaji_20181204_室外_15-111_51_gray_503.jpg']
        arrlen = len(imgarr)
        print(imgarr)
        for i in range(arrlen):
            a = imgarr[i].strip()
            print(a)
            if not os.path.exists(a):
                continue
            img = Image.open(a)
            # print(imgarr[i].strip())
            imga = ImageTk.PhotoImage(img)
            self.imgpath.append(imga)
            # label = ttk.Label(self.tp, image=self.imgpath[i])
            label = ttk.Label(self.tp)
            self.labelarr.append(label)
            self.labelarr[i]['image'] = self.imgpath[i]
            self.labelarr[i].grid(row=0, column=i)
            self.labelarr[i].bind("<Button-1>", self.handlerAdaptor(self.callback, a=i))

    def handlerAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def callback(self, event, a):
        print('click' + str(a))

        # self.tp.protocol("WM_DELETE_WINDOW", self.on_tpclose)
        # label.grid(row=0, column=0)
        # label1 = ttk.Label(self.tp, image=self.imgpath[1])
        # label1.grid(row=0, column=1)
        # self.labelarr.append(label)
        # self.labelarr[i].grid(row=0, column=i)
    # def on_tpclose(self):
    #     self.imgpath=None
    #     self.labelarr=None
    #     print('tp del')


if __name__ == '__main__':
    root = tk.Tk()

    root.title('EX')
    # root.geometry('850x850')
    # root.resizable(width=False, height=False)  # 是否允许改变大小
    App(root)
    root.mainloop()
