# -*- coding: UTF-8 -*-

import csv
import os,stat
import urllib
import sys

txt_path = './txt'
img_path = './img'
suffix = ['.jpg','.png','.jpeg','.bmp']

def writeTxt(filename,info):
    try:
        if not os.path.exists(txt_path):
            os.makedirs(txt_path)
        filename = txt_path+'/'+str(filename)
        f = open(filename,'a')
        f.write(str(info)+'\n')
    except Exception as e:
        print("Error:没有找到文件或读取文件失败！！%s"%e)
        return 0
    else:
        f.close()
        return 1


def callback(blocknum, blocksize, totalsize):
    '''
    :param blocknum: 已下载数据块
    :param blocksize: 数据块大小
    :param totalsize: 远程文件大小
    :return:
    '''
    percent = 100.0*blocknum*blocksize/totalsize
    if(percent>100):
        percent = 100
    sys.stdout.write('\r'+'%.2f%%' % percent)
    sys.stdout.flush()

def downloadImg(img_url,pid,cid,rect):
    try:
        pid = '%06d'%pid
        cid = 'IMDbFace_'+pid+'_'+'%04d'%cid

        img_pathd = img_path+'/'+str(pid)
        if not os.path.exists(img_pathd):
            os.makedirs(img_pathd)
        file_suffix = os.path.splitext(img_url)[1]
        if file_suffix in suffix:
            filename = '{}{}{}{}'.format(img_pathd,os.sep,cid,file_suffix)
        else:
            file_suffix = '.jpg'
            filename = '{}{}{}{}'.format(img_pathd,os.sep,cid,file_suffix)
        print(filename)
        print(img_url)
        
        #urllib.request.urlretrieve(img_url,filename=filename,reporthook=callback)
        urllib.urlretrieve(img_url,filename=filename,reporthook=callback)
    except IOError as e:
        print('1%s'%e)
        return 0
    except Exception as e:
        print('2%s'%e)
        return 0
    else:
        txt_name =str(pid)+'.txt'
        info = filename+'  '+rect
        
        #statue = writeTxt()
        return writeTxt(txt_name,info)

def main():
    csv_file = csv.reader(open('IMDb-Face.csv','r'))
    csv_list = list(csv_file)
    pname1 = ''
    a=0
    for i in range(len(csv_list)):
        pname2 = csv_list[i+1][1]
        if pname1 == pname2:
            b = b+1
            statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
            if statu==1:
                print("写入文件成功！！")
            else:
                print("下载失败！！")
        else:
            b=1
            a = a+1
            pname1 = pname2
            statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
            if statu==1:
                print("写入文件成功！！")
            else:
                print("下载失败！！")

if __name__ == '__main__':
    main()
   
