import csv
import os,stat
import urllib.request
import sys
import socket
import profile

txt_path = './txt'win
img_path = './img'
suffix = ['.jpg','.png','.jpeg','.bmp']
#设置下载超时时间为60s
socket.setdefaulttimeout(60)


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
        urllib.request.urlretrieve(img_url,filename=filename,reporthook=callback)
       
    except IOError as e:
        print('1%s'%e)
        return 0
    except urllib.request.HTTPError as e:
        

    except socket.timeout:
        count = 1
        while count <=5:
            try:
                urllib.request.urlretrieve(img_url,filename=filename,reporthook=callback)
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d time'%count
                print(err_info)
                count += 1
        if count > 5:
            return 0
    except Exception as e:
        print('2%s'%e)
        return 0
    else:
        txt_name =str(pid)+'.txt'
        info = filename+'  '+rect
        
        #statue = writeTxt()
        return writeTxt(txt_name,info)

def download_a(csv_list,c,process_num):
    pname1 = ''
    a=0 #用来记录人的编号
    b=0 #用来记录每个人的图片编号
    d=c
    for i in range(len(csv_list)):
        pname2 = csv_list[i+1][1]
        
        if pname1 == pname2:
            b = b+1
            if a>d:
                statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
                if statu==1:
                    print("写入文件成功！！\n\n")
                else:
                    print("下载失败！！\n\n")
        else:
            b=1
            a = a+1
            pname1 = pname2
            if a>c:
                c+=process_num
                statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
                if statu==1:
                    print("写入文件成功！！\n\n")
                else:
                    print("下载失败！！\n\n")

def main():
    csv_file = csv.reader(open('IMDb-Face.csv','r'))
    csv_list = list(csv_file)
    c=0 #用来记录下载开始人的编号

    fork1 = os.fork()
    fork2 = os.fork()
    fork3 = os.fork()
    if fork1 == 0:
        if fork2 == 0:
            if fork3 == 0:
                download_a(csv_list,c,8)
            else:
                download_a(csv_list,c+1,8)
        else:
            if fork3 == 0:
                download_a(csv_list,c+2,8)
            else:
                download_a(csv_list,c+3,8)
    else:
        if fork2 == 0:
            if fork3 == 0:
                download_a(csv_list,c+4,8)
            else:
                download_a(csv_list,c+5,8)
        else:
            if fork3 == 0:
                download_a(csv_list,c+6,8)
            else:
                download_a(csv_list,c+7,8)
    '''
    for i in range(len(csv_list)):
        pname2 = csv_list[i+1][1]
        
        if pname1 == pname2:
            b = b+1
            if a>357:
                statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
                if statu==1:
                    print("写入文件成功！！\n\n")
                else:
                    print("下载失败！！\n\n")
        else:
            b=1
            a = a+1
            pname1 = pname2
            if a>357:
                
                statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
                if statu==1:
                    print("写入文件成功！！\n\n")
                else:
                    print("下载失败！！\n\n")
    '''

if __name__ == '__main__':
    main()
   
