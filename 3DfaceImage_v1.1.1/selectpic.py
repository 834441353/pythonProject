import os

inpath = '/datasdc/img_celeba_select'
outpath = '/datasdc/img_celeba_select1'

filelist = os.listdir(inpath)
filelistlen = len(filelist)
a = 1
b = 0
for i in range(filelistlen):
    afile = os.path.join(inpath, filelist[i])
    bpath = os.path.join(outpath, str(b), 'gls')
    if not os.path.exists(bpath):

        os.makedirs(bpath)
    bfile = os.path.join(bpath, filelist[i])
    command = 'mv ' + afile + ' ' + bfile
    os.system(command)
    print(command)
    if a != 10:
        a += 1
        continue
    b += 1
    a = 1
