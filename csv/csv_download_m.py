import csv
import os,stat
import urllib.request
import sys
import socket
from multiprocessing import Pool

txt_path = './txt'
img_path = './img'
suffix = ['.jpg','.png','.jpeg','.bmp']
#设置下载超时时间为45s
socket.setdefaulttimeout(45)


def writeTxt(filename,info):
    try:
        if not os.path.exists(txt_path):
            os.makedirs(txt_path)
        filename = txt_path+'/'+str(filename)
        f = open(filename,'a')
        f.write(str(info)+'\n')
        f.close()
    except Exception as e:
        print("Error:没有找到文件或读取文件失败！！%s"%e)
        return 0
    else:
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
        pid = '%06d'%(pid)
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
    except urllib.error.HTTPError as e:
        print('%s  img_url = %s'%(e,img_url))
        if e.code == 404:
            count = 1
            while count <=3:
                try:
                    urllib.request.urlretrieve(img_url,filename=filename,reporthook=callback)
                except urllib.error.HTTPError as e:
                    count += 1
                except socket.timeout:
                    count += 1
                except Exception as e:
                    count += 1
                else:
                    txt_name =str(pid)+'.txt'
                    info = filename+'  '+rect
                    return writeTxt(txt_name,info)
            if count > 3:
                return 0
    except IOError as e:
        print('%s  img_url = %s'%(e,img_url))
        return 0
    except socket.timeout:
        count = 1
        while count <=5:
            try:
                urllib.request.urlretrieve(img_url,filename=filename,reporthook=callback)
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d time'%count
                print(err_info)
                count += 1
            except Exception as e:
                count += 1
            else:
                txt_name =str(pid)+'.txt'
                info = filename+'  '+rect
        
                #statue = writeTxt()
                return writeTxt(txt_name,info)
        if count > 5:
            return 0
    except Exception as e:
        print('%s  img_url = %s'%(e,img_url))
        return 0
    else:
        txt_name =str(pid)+'.txt'
        info = filename+'  '+rect
        
        #statue = writeTxt()
        return writeTxt(txt_name,info)

def mid(img_url,pid,cid,rect):
    statu = downloadImg(img_url,pid,cid,rect)
    if statu == 1:
        print('写入文件成功！！\n')
    else:
        print('下载失败！！\n')


def main():
    csv_file = csv.reader(open('IMDb-Face.csv','r'))
    csv_list = list(csv_file)
    po = Pool(10)
    pname1 = ''
    a=-1
    for i in range(len(csv_list)):
        pname2 = csv_list[i][1]
        
        if pname1 == pname2:
            b = b+1
            if a>39009:
                po.apply_async(mid,(csv_list[i][5],a,b,csv_list[i][3],))
                
                '''
                statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
                if statu==1:
                    print("写入文件成功！！\n\n")
                else:
                    print("下载失败！！\n\n")
                '''
        else:
            b=1
            a = a+1
            pname1 = pname2
            if a>39009:
                po.apply_async(mid,(csv_list[i][5],a,b,csv_list[i][3],))
                
                '''
                statu = downloadImg(csv_list[i+1][5],a,b,csv_list[i+1][3])
                if statu==1:
                    print("写入文件成功！！\n\n")
                else:
                    print("下载失败！！\n\n")
                '''
    po.close()
    po.join()

if __name__ == '__main__':
    main()
   
