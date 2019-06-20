import cv2
import os

inpath = './3d'
txtpath = './1.txt'

txtcontext = []
for i in os.listdir(inpath):
    apath = os.path.join(inpath, i)
    for j in os.listdir(apath):
        if j == 'Bmp':
            bpath = os.path.join(apath, j)
            for f in os.listdir(bpath):
                filepath = os.path.join(bpath, f)
                img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
                if len(img.shape) == 2:
                    filetype = filepath + '  2\n'
                    txtcontext.append(filetype)
                elif len(img.shape) == 3:
                    filetype = filepath + '  3\n'
                    txtcontext.append(filetype)
                else:
                    print(filepath)
with open(txtpath, 'a+') as fb:
    for z in txtcontext:
        fb.writelines(z)
