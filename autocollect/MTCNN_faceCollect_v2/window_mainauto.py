#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#  @author:  peng tao
# 
#    Mar 14, 2018 14:53:45 PM

#from tkinter import*
from tkinter import filedialog as fdialog
from tkinter.dialog import*
from tkinter.messagebox import*
import tkinter.ttk as ttk
py3 = 1
#import camera_single_face 
from VideoCapture import Device
import cv2
import numpy
import os
#import threading
import winsound
import detect_face

#winsound.Beep(100,500)

#PlaySound(sound)

path0 = os.getcwd()
father_path=os.path.abspath(os.path.dirname(path0)+os.path.sep+".")

saveimagepath = os.path.join(father_path,'collectImagequick')
if not os.path.exists(saveimagepath):
    os.mkdir(saveimagepath)
    #os.makedirs()
#imagepathnum = 0

imagepathnum = len(os.listdir(saveimagepath))


def save_file():
    pass
    '''
    file=fdialog.asksaveasfile(mode="wb", title="Save Figure", defaultextension=".png", filetypes = (("png files","*.png"),("all files","*.*")))
    if file is None:
        return None
    img_to_save=open(".temp/generated_plot.png","rb").read()
    file.write(img_to_save)
    file.close()
    '''
def showAbout():
        showinfo("face detect version 1.0","quit key: 'q','Esc'\n directiong key:'2''4''6''8'\n delete key :'d'\n save key:'s'\n data: 2018/3/20 \n, other maybe call me 110114112")

class Menubar:
    def __init__(self, master):       
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save", command=save_file)
        filemenu.add_command(label="Quit", command=root.destroy)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About facedetect",command= showAbout)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

def destroy_app():
    global root
    root.destroy()
    exit(0)
# global colors variables for theme switch
_activebgcolordark = '#808080'
_bgcolorlight = '#ffffff'
_fgcolorlight = '#000000'
_lightwindowbackground = '#f2f2f2'

def callback(event): 
    print("当前位置：",event.x,event.y)
    print(event.char)
    if event.x>543 and event.y>525:
        return
    savePicmethod()

class New_Toplevel_1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        top.geometry("640x660+408+185")#("555x398+408+185")  x  y 
        top.title("collectfaceapp")
        #frame = Frame(app, width = 200, height = 200)
        #frame.bind("<Motion>",callback)
        top.bind("<Button-1>",callback)
        top.bind("<Button-2>",callback)
        top.bind("<Button-3>",callback)
        top.bind("<Key>",callback)
        top.focus_set()
       
        
        root.configure(background=_lightwindowbackground)

        self.next = Button(top)
        self.next.place(relx=0.86, rely=0.80 , height=50, width=70)
        self.next.configure(activebackground=_activebgcolordark)
        self.next.configure(command=lambda: self.detectDot(1))
        self.next.configure(cursor="left_ptr")
        self.next.configure(text='face_de')
        #self.next.configure(width=47)
        self.next.configure(background=_bgcolorlight)
        self.next.configure(fg=_fgcolorlight)
        
 
        self.auto = Button(top)
        self.auto.place(relx=0.86, rely=0.90, height=50, width=70)
        self.auto.configure(activebackground=_activebgcolordark)
        self.auto.configure(command=lambda: self.fastCollect())
        self.auto.configure(cursor="left_ptr")
        self.auto.configure(text='fast')
        #self.auto.configure(width=47)
        self.auto.configure(background=_bgcolorlight)
        self.auto.configure(fg=_fgcolorlight)
    
    


    
    def detectDot(self,method):
        print('not add ')
        pass
                
    def fastCollect(self):
        savePicmethod()
    
    
    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)

def Manage_main():
    """ inter the main routine"""
    global  root
    root=Tk()
    #root.state("zoomed")
    root.resizable(width=False, height=False)
    top = New_Toplevel_1(root)
    m = Menubar(root)
    root.protocol('WM_DELETE_WINDOW', destroy_app)
    root.mainloop()



singleFoldNum = 600

def savePicmethod():
    pic_num =0
    global imagepathnum
    global saveimagepath
    cap = Device(0)
    cap1 = Device(1)
    if cap is None :
        
        winsound.Beep(50,400)
        return
    if cap1 is None:
       
        winsound.Beep(50,400)
        return
    '''
    if not ret :
        print('camera 1 is not OK!')
    if not ret1:
        print('camera 2 is not OK!')
    '''
    #while ret and ret1:
    while 1:
        '''
        ret, frame = cap.read()
        ret1, frame1 = cap1.read()
        '''
        frame = cap.getImage()
        frame = cv2.cvtColor(numpy.asarray(frame),cv2.COLOR_RGB2BGR)
        #frameor = frame
        frame1 = cap1.getImage()
        frame1 = cv2.cvtColor(numpy.asarray(frame1),cv2.COLOR_RGB2BGR)
        #frame1or = frame1
        
        save_color_path = os.path.join(saveimagepath,'%s/color'%imagepathnum)
        if not os.path.exists(save_color_path):
            os.makedirs(save_color_path)
        save_gray_path = os.path.join(saveimagepath,'%s/gray'%imagepathnum)
        if not os.path.exists(save_gray_path):
            os.mkdir(save_gray_path)
        
        color_file = os.path.join(save_color_path, "%s.jpg"%pic_num)
        gray_file = os.path.join(save_gray_path, "%s.jpg"%pic_num)

        cv2.imwrite(color_file, frame)
        cv2.imshow('clor',frame)
        cv2.imshow('gray',frame1)
        cv2.waitKey(3)#
        cv2.imwrite(gray_file, frame1)
        pic_num+=1
        if pic_num>singleFoldNum:
            pic_num = 0
            print('collect fold num %s OK!'%imagepathnum)
            imagepathnum +=1
            cv2.destroyAllWindows()
            break 

    winsound.Beep(100,500)


if __name__ == "__main__":
    Manage_main()
