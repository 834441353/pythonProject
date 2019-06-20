import os

inpath = './k01_datahome/20190521'
outpath = './k01_datahome_2'
c = 0

inpathlist = os.listdir(inpath)

for i in range(len(inpathlist)):
    c += 1
    a = os.path.join(inpath, inpathlist[i])
    d = os.listdir(a)
    for j in range(len(d)):
        e = os.path.join(a, d[j])
        b = os.path.join(outpath, str(('%07d' % c)))
        if not os.path.exists(b):
            os.makedirs(b)
        command = 'mv '+e+' '+b
        os.system(command)
        print(command)
