from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('python')

img = Image.open('datahome_zhaji_20181204_8-44_8_gray_25.jpg')  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
imglabel = ttk.Label(root, image=photo)
imglabel.grid(row=0, column=0, columnspan=3)



root.mainloop()