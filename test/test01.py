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
import cv2


class app:
    def __init__(self, root):
        self.img = Image.open('datahome_zhaji_20181204_8-44_8_gray_25.jpg')  # 打开图片
        self.photo = ImageTk.PhotoImage(self.img)  # 用PIL模块的PhotoImage打开
        self.imglabel = ttk.Label(root, image=self.photo)
        self.imglabel.grid(row=0, column=0, columnspan=3)
        print('app')
        print(self.img)


        # self.but = ttk.Button(root, text='a')
        # self.but.grid(row=0, column=1)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('python')
    app(root)
    root.mainloop()
