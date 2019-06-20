import os

inpath = './k01_datahome/20190521'
outpath = './k01_datahome_2'

for i in os.listdir(inpath):
    a = os.path.join(inpath,i)
    print(a)