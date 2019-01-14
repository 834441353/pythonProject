import csv
import os

txt_path = './txt/'

def main():
    csv_dict = {}
    csv_file = csv.reader(open('IMDb-Face.csv','r'))
    csv_list = list(csv_file)
    for i in range(len(csv_list)):
        csv_rect = csv_list[i][3]
        csv_size = csv_list[i][4]
        csv_dict[csv_rect] = csv_size
   
    for f in os.listdir(txt_path):
        filename = txt_path+f
        with open(filename,'r') as f1,open("%s.bak"%filename,'w') as f2:
            for line in f1.readlines():
                rect = line.strip().split('  ')[1]
                size = csv_dict[rect]
                info = line.strip().split('  ')[0]+'  '+line.strip().split('  ')[1]+'  '+size
                f2.write(info+'\n')
            os.remove(filename)
            os.rename("%s.bak"%filename,filename)

                #print(size)
                #print(csv_file_list.index(rect))

if __name__=='__main__':
    main()