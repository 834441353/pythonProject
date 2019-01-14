#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#  @author:  peng tao
# 
#    Mar 14, 2018 14:53:45 PM

# from tkinter import*
from tkinter import filedialog as fdialog
from tkinter.dialog import *
from tkinter.messagebox import *
import tkinter.ttk as ttk

py3 = 1
# import camera_single_face
from VideoCapture import Device
import cv2
import numpy as np
import os
# import threading
import winsound
import datetime
import detect_face
import tensorflow as tf

# winsound.Beep(100,500)

# PlaySound(sound)

start_h = 10
start_m = 54
end_h = 10
end_m = 55
start_h2 = 10
start_m2 = 56
end_h2 = 10
end_m2 = 57

path0 = os.getcwd()
father_path = os.path.abspath(os.path.dirname(path0) + os.path.sep + ".")

saveimagepath = os.path.join(father_path, 'collectImagequick')
if not os.path.exists(saveimagepath):
    os.mkdir(saveimagepath)
    # os.makedirs()
# imagepathnum = 0

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
    showinfo("face detect version 1.0",
             "quit key: 'q','Esc'\n directiong key:'2''4''6''8'\n delete key :'d'\n save key:'s'\n data: 2018/3/20 \n, other maybe call me 110114112")


class Menubar:
    def __init__(self, master):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save", command=save_file)
        filemenu.add_command(label="Quit", command=root.destroy)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About facedetect", command=showAbout)
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
    print("当前位置：", event.x, event.y)
    print(event.char)
    if event.x > 543 and event.y > 525:
        return
    # savePicmethod()


# class MTCNN_Face():

def to_rgb(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = img
    return ret


class MTCNN_Face():
    def __init__(self):
        try:
            tf.Graph().as_default()
            gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)
            sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
            try:
                sess.as_default()
                self.pnet, self.rnet, self.onet = detect_face.create_mtcnn(sess, None)
            except:
                pass
        except:
            pass
        self.minsize = 20  # minimum size of face
        self.threshold = [0.6, 0.6, 0.7]  # three steps's threshold
        self.factor = 0.709  # scale factor
        self.bb = np.zeros(4, dtype=np.int32)
        self.eye_bb = np.zeros(10, dtype=np.int32)
        self.shapebb = np.zeros(136, dtype=np.int32)

    def detectFeature(self, img):
        if img is None:
            return None
        else:
            if img.ndim == 2:
                img = to_rgb(img)
            img = img[:, :, 0:3]

            bounding_boxes, points = detect_face.detect_face(img, self.minsize, self.pnet, self.rnet, self.onet,
                                                             self.threshold, self.factor)
            # 检测到人脸的个数
            nrof_faces = bounding_boxes.shape[0]
            if nrof_faces == 0:
                return nrof_faces, 0
            lev = np.round(bounding_boxes[0, :][4], 2)

            # print(bounding_boxes)
            # for i in range(nrof_faces):
            #
            #     det = bounding_boxes[i, :]
            #     if float(det[4]) >= float(0.95):
            #         det = bounding_boxes[i]
            #
            #         # spoint = points[:, i]
            #         # print(points, '---', spoint)
            #
            #         # cv2.putText(img, str(np.round(det[4], 2)), (int(det[0]), int(det[1])), cv2.FONT_HERSHEY_TRIPLEX,
            #         #             1, color=(255, 0, 255))
            #         # cv2.rectangle(img, (int(det[0]), int(det[1])), (int(det[2]), int(det[3])), (0, 0, 255))
            #         # for kk in range(5):
            #         #     cv2.circle(img, (spoint[kk], spoint[kk + 5]), 2, (0, 255, 255), -1)
            #         #     cv2.putText(img, "%d" % (kk), (spoint[kk], spoint[kk + 5]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5,(255, 255, 0))
            return nrof_faces, lev


class New_Toplevel_1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        top.geometry("640x660+408+185")  # ("555x398+408+185")  x  y
        top.title("collectfaceapp")
        # frame = Frame(app, width = 200, height = 200)
        # frame.bind("<Motion>",callback)
        top.bind("<Button-1>", callback)
        top.bind("<Button-2>", callback)
        top.bind("<Button-3>", callback)
        top.bind("<Key>", callback)
        top.focus_set()

        root.configure(background=_lightwindowbackground)

        self.next = Button(top)
        self.next.place(relx=0.86, rely=0.80, height=50, width=70)
        self.next.configure(activebackground=_activebgcolordark)
        # self.next.configure(command=lambda: self.detectDot(1))
        self.next.configure(command=lambda: destroy_app())
        self.next.configure(cursor="left_ptr")
        self.next.configure(text='face_de')
        # self.next.configure(width=47)
        self.next.configure(background=_bgcolorlight)
        self.next.configure(fg=_fgcolorlight)

        self.auto = Button(top)
        self.auto.place(relx=0.86, rely=0.90, height=50, width=70)
        self.auto.configure(activebackground=_activebgcolordark)
        self.auto.configure(command=lambda: self.fastCollect())
        self.auto.configure(cursor="left_ptr")
        self.auto.configure(text='fast')
        # self.auto.configure(width=47)
        self.auto.configure(background=_bgcolorlight)
        self.auto.configure(fg=_fgcolorlight)
        self.cap = Device(0)
        self.cap1 = Device(1)
        self.mtf = MTCNN_Face()

    def detectDot(self, method):
        print('not add ')
        pass

    def fastCollect(self):

        while True:
            now = datetime.datetime.now()
            # 
            if (now.hour == start_h and now.minute == start_m) or (now.hour == start_h2 and now.minute == start_m2):
                print(now.strftime('%H:%M:%S'))
                print('start')
                savePicmethod(self.cap,self.cap1,self.mtf)

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)


def Manage_main():
    """ inter the main routine"""
    global root
    root = Tk()
    # root.state("zoomed")
    root.resizable(width=False, height=False)
    top = New_Toplevel_1(root)
    m = Menubar(root)
    root.protocol('WM_DELETE_WINDOW', destroy_app)
    root.mainloop()


singleFoldNum = 600


def savePicmethod(cap,cap1,mtf):
    pic_num = 0
    global imagepathnum
    global saveimagepath

    if cap is None:
    	return
    if cap is None:
    	return
    
    '''
    if not ret :
        print('camera 1 is not OK!')
    if not ret1:
        print('camera 2 is not OK!')
    '''
    # while ret and ret1:
    flag = 1
    while 1:
        '''
        ret, frame = cap.read()
        ret1, frame1 = cap1.read()
        '''
        frame = cap.getImage()
        if frame is None:
        	print('frame is none!!')
        	continue
        frame = cv2.cvtColor(np.asarray(frame), cv2.COLOR_RGB2BGR)
        # frameor = frame
        frame1 = cap1.getImage()
        if frame1 is None:
        	print('frame1 is None!!')
        	continue
        frame1 = cv2.cvtColor(np.asarray(frame1), cv2.COLOR_RGB2BGR)
        # frame1or = frame1

        if flag == 1:
            now = datetime.datetime.now()
            if (now.hour == end_h and now.minute == end_m) or (now.hour == end_h2 and now.minute == end_m2):
                print(now.strftime('%H:%M:%S'))
               
                cv2.destroyAllWindows()
                print('del')
                # destroy_app()
                break
            height, width = frame.shape[:2]
            # frame3 = cv2.resize(frame, (int(width / 2), int(height / 2)), 0, 0, interpolation=cv2.INTER_AREA);

            num_faces, lev = mtf.detectFeature(frame)
            print(lev)
            cv2.imshow('frame', frame)
            cv2.waitKey(3)  #

            if num_faces == 0:
                continue
            if lev<0.8:
                continue
            flag = 0
        save_color_path = os.path.join(saveimagepath, '%s/color' % imagepathnum)
        if not os.path.exists(save_color_path):
            os.makedirs(save_color_path)
        save_gray_path = os.path.join(saveimagepath, '%s/gray' % imagepathnum)
        if not os.path.exists(save_gray_path):
            os.mkdir(save_gray_path)

        color_file = os.path.join(save_color_path, "%s.jpg" % pic_num)
        gray_file = os.path.join(save_gray_path, "%s.jpg" % pic_num)

        cv2.imwrite(color_file, frame)
        cv2.imshow('clor', frame)
        cv2.imshow('gray', frame1)
        cv2.waitKey(3)  #
        cv2.imwrite(gray_file, frame1)
        pic_num += 1
        # if pic_num>singleFoldNum:

        if pic_num > 600:
            imagepathnum += 1
            print('collect fold num %s OK!' % imagepathnum)
            flag = 1
            pic_num = 0
            continue

    # winsound.Beep(100, 500)


if __name__ == "__main__":
    Manage_main()
