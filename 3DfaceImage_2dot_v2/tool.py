import os

inpath = './20190521'
outpath = './depth'

onelsit = os.listdir(inpath)
for i in onelsit:
    onepath = os.path.join(inpath, i)
    twolist = os.listdir(onepath)
    for j in twolist:
        if j == 'dep':
            twopath = os.path.join(onepath, j)
            b = os.path.join(outpath, i, )
            if not os.path.exists(b):
                os.makedirs(b)

            command = 'cp -r ' + twopath + ' ' + b
            os.system(command)
            print(command)
