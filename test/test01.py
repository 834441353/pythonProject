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

# import tkinter as tk
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
# import cv2
# import copy
#
#
# class app:
#     def __init__(self, root):
#         self.img = Image.open('datahome_zhaji_20181204_8-44_8_gray_25.jpg')
#         self.photo = ImageTk.PhotoImage(self.img)
#         self.imglabel = ttk.Label(root, image=self.photo)
#         # self.imglabel.configure(image=self.photo)
#         self.imglabel.grid(row=0, column=0)
#
#         # but1 = ttk.Button(root, text=str(1))
#         # but1.grid(row=0, column=1)
#         # but2 = ttk.Button(root, text=str(2))
#         # but2.grid(row=0, column=2)
#         # but3 = ttk.Button(root, text=str(3))
#         # but3.grid(row=0, column=3)
#         # but4 = ttk.Button(root, text=str(4))l
#         # but4.grid(row=0, column=4)
#
#         print(self.img)
#         self.bunarr = []
#         for i in range(5):
#             but = ttk.Button(root, text=str(i), command=lambda: self.butc(i))
#             print(i)
#             self.bunarr.append(but)
#             self.bunarr[i].config(command=lambda: self.butc(i))
#             self.bunarr[i].grid(row=0, column=i + 1)
#         # root.mainloop()
#
#     def butc(self, num):
#         # self.mymessage(num)
#         msg = tk.Message(root, text='a')
#         msg.grid()
#
#     def mymessage(self, msg):
#         messagebox.showinfo('button num', msg)
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title('python')
#     app(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
#
# root = tk.Tk()
#
# def on_closing():
#
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.destroy()
#
# root.protocol("WM_DELETE_WINDOW", on_closing)
# root.mainloop()

# from tkinter import *
#
# root = Tk()
#
#
# def key(event):
#     print("pressed", repr(event.char))
#
#
# def callback(event):
#     frame.focus_set()
#     print("clicked at", event.x, event.y)
#
#
# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()
#
# root.mainloop()
