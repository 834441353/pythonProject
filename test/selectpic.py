import os
import random

inpath = 'T:/testpic'
outpath = 'T:/chosepath'

flist = os.listdir(inpath)
flistlen = len(flist)
for i in range(flistlen):
    a = os.path.join(inpath, flist[i])
    if os.path.isfile(a):
        continue
    secondlist = os.listdir(a)
    secondlistlen = len(secondlist)
    for j in range(secondlistlen):
        b = os.path.join(a, secondlist[j])
        if os.path.isfile(b):
            continue
        filelist = os.listdir(b)
        filelistlen = len(filelist)
        x = int(float(filelistlen) * 0.0056)
        choselist = random.sample(filelist, x)
        for z in range(x):
            c = os.path.join(b, choselist[z])
            outfilepath = os.path.join(outpath, flist[i], secondlist[j])
            if not os.path.exists(outfilepath):
                os.makedirs(outfilepath)
            outfile = os.path.join(outfilepath, choselist[z])
            command = 'cp ' + c + ' ' + outfilepath
            os.system(command)
            print(command)

