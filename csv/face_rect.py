import cv2
import os
from multiprocessing import Pool
import time

txt_path = './txt/'
txt_savepath = './txt_ta/'
img_savepath = './img_ta/'

#在原图中标记人脸的位置
def draw_rect(filename,rect_list,size_list):
	img = cv2.imread(filename)
	sp = img.shape
	#print(size_list)
	#print(str(sp[0])+' '+str(sp[1]))
	mul1 = float(sp[0])/float(size_list[0])
	#mul2 = float(sp[1])/float(size_list[1])
	#print(str(mul1)+'  '+str(mul2))
	#newfilename ="." + filename.split(".")[-2]+"_rect."+filename.split(".")[-1]
	left =int(float(rect_list[0])*mul1)#2
	top = int(float(rect_list[1])*mul1)
	right = int(float(rect_list[2])*mul1)#2
	bottom = int(float(rect_list[3])*mul1)
	#print(left+' '+top+' '+right+' '+bottom+'  '+newfilename)
	
	start = (left ,top)
	end = (right ,bottom)

	
	color = (25,255,255)
	cv2.rectangle(img,start,end,color,3)
	cv2.imwrite(filename,img)

#在原图中标记人脸的位置
def draw_rect2(filename,rect_list):
	print(filename)
	img = cv2.imread(filename)
	sp = img.shape
	
	left =int(rect_list[0])
	top = int(rect_list[1])
	right = int(rect_list[2])
	bottom = int(rect_list[3])
	
	
	start = (left ,top)
	end = (right ,bottom)

	
	color = (25,255,255)
	cv2.rectangle(img,start,end,color,3)
	cv2.imwrite(filename,img)


#裁剪face图片
def tailor(filename,rect_list,size_list):
	
	img = cv2.imread(filename)
	#sp = img.shape
	h = img.shape[0]
	w = img.shape[1]
	rect_list_ta = ['','','','']
	mul2 = float(w)/float(size_list[1])
	left =float(rect_list[0])*mul2#2
	top = float(rect_list[1])*mul2
	right = float(rect_list[2])*mul2#2
	bottom = float(rect_list[3])*mul2
	rowN = float(right-left)/2
	colN = float(bottom-top)/2
	#img_t = img[int(left-rowN):int(right+rowN),int(top-colN):int(bottom+colN)]
	#left
	leftN = int(left-rowN) 
	rect_list_ta[0] = int(rowN)
	if int(left-rowN)<0:
		leftN= 0
		rect_list_ta[0] = int(left)
	#top
	topN = int(top-colN) 
	rect_list_ta[1] = int(rowN)
	if int(top-colN)<0:
		topN = 0
		rect_list_ta[1] = int(top)
	#right
	rightN = int(right+rowN)
	rect_list_ta[2] = rect_list_ta[0]+int(2*rowN)
	#bottom
	bottomN = int(bottom+colN)
	rect_list_ta[3] = rect_list_ta[1]+int(2*colN)
	img_t = img[topN:bottomN,leftN:rightN]
	path = img_savepath+filename.split('/')[-2]+'/'
	if not os.path.exists(path):
		os.makedirs(path)
	newfilename = path+filename.split('/')[-1]
	#newfilename ="." + filename.split(".")[-2]+"_ta."+filename.split(".")[-1]
	cv2.imwrite(newfilename,img_t)
	print(newfilename+'  '+str(rect_list_ta))
	txt_name = filename.split('/')[2]+'.txt'
	txt_info = newfilename+'  '+str(rect_list_ta[0])+' '+str(rect_list_ta[1])+' '+str(rect_list_ta[2])+' '+str(rect_list_ta[3])
	#print(txt_name)
	#print(txt_info)
	writeTxt(txt_name,txt_info)
	#os.remove(newfilename)


def writeTxt(filename,info):
    try:
        if not os.path.exists(txt_savepath):
            os.makedirs(txt_savepath)
        filename = txt_savepath+'/'+str(filename)
        f = open(filename,'a')
        f.write(str(info)+'\n')
        f.close()
    except Exception as e:
        print("Error:没有找到文件或读取文件失败！！%s"%e)
        return 0
    else:
        return 1

'''
#143 246 608 719   ['429','738','1824','2109']
draw_rect('./img/000001/IMDbFace_000001_0002.jpg',['429','738','1824','2109'])
'''

def main():
	po = Pool(4)
	time1 = time.time()
	for i in os.listdir(txt_path):
		with open(txt_path+i,'r') as f :
			for line in f.readlines():
				filename = line.strip().split("  ")[0]
				rect_list = line.strip().split("  ")[1].split(" ")
				size_list = line.strip().split("  ")[2].split(" ")
				#draw_rect(filename,rect_list,size_list)
				#tailor(filename,rect_list,size_list)
				po.apply_async(tailor,(filename,rect_list,size_list,))
				#po.apply_async(draw_rect2,(filename,rect_list,))
			f.close()
	po.close()
	po.join()
	time2 = time.time()
	print(time2-time1)

if __name__ == '__main__':
	main()