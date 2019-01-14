import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

from PIL import Image
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
        # self.lbf = ttk.LabelFrame(root, text='img',padx=5, pady=5 )

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
            self.loadimg(file.readlines())

    def mywaringmessaeg(self, message):
        messagebox.showwarning('Python Message Warning Box', message)

    def loadimg(self, imgarr):
        self.tp = tk.Toplevel()
        arrlen = len(imgarr)
        for i in range(arrlen):
            img_open = Image.open(arrlen[i])
            label = ttk.Label(self.tp, image=img_open)
            label.grid(row=0, column=i)


if __name__ == '__main__':
    root = tk.Tk()

    root.title('EX')
    # root.geometry('850x850')
    # root.resizable(width=False, height=False)  # 是否允许改变大小
    App(root)
    root.mainloop()
