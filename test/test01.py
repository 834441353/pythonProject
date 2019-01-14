# import sys
# import os,stat
#
# path = './txt'
# def write_txt(filename ,id):
#     try:
#         if not os.path.exists(path):
#             os.makedirs(path)
#         filename = path+'/'+str(filename)
#         f = open(filename,'a')
#         f.write(str(id)+'\n')
#
#
#     except Exception as e:
#         print("Error:没有找到文件或读取文件失败！！%s"%e)
#         return 0
#     else:
#         print("写入文件成功！！")
#         f.close()
#         return 1
#
#
#
# if __name__ == '__main__':
#     for i in range(6):
#         write_txt('01.txt',i)

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class app():
    def __init__(self, root):
        self.width = 160
        self.height = 160
        self.imgpath = 'datahome_zhaji_20181204_暗室_8-44_8_gray_25.jpg'
        img = Image.open(self.imgpath)
        imga = ImageTk.PhotoImage(img.resize((self.width, self.height)))
        # imga = tk.PhotoImage(self.imgpath)
        self.label = ttk.Label(root, image=imga)
        self.label.grid(row=0, column=0)

        self.but = ttk.Button(root, text='a')
        self.but.grid(row=0, column=1)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('EX')
    root.geometry('850x850')
    # root.resizable(width=False, height=False)  # 是否允许改变大小
    app(root)
    root.mainloop()
