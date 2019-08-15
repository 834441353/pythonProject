import os
import cv2
import numpy

inpath = 'Y:/datahome/3d/Negative_sample/20190619/BW'

inpathlist = os.listdir(inpath)
for i in inpathlist:
    apath = os.path.join(inpath, i)
    for j in os.listdir(apath):
        if j != 'Png':
            continue
        bpath = os.path.join(apath,j)
        command = 'rm -r '+bpath
        os.system(command)
        print(command)
