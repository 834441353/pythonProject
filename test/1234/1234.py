import os


# 3D数据处理  将3D采集的gray数据特征点映射到相邻的depth图片中
# 注：txt文件将在自身发生变化，注意备份
#     txt文件中的图片路径为绝对路径，运行前虚修改路径
# 参数：处理的txt文件夹目录
def feature_gray2color(inpath):
    # inpath = './BW_txt'

    txtlist = os.listdir(inpath)
    contexts = []
    for i in txtlist:
        a = os.path.join(inpath, i)
        with open(a, 'r') as fb:
            lines = fb.readlines()
            for j in range(len(lines)):
                b = int(lines[j].strip().split(' ')[0].split('.')[0].split('_')[-1])
                if b % 2 == 0:
                    b = b - 1
                    filename = '_'.join(lines[j].strip().split('_')[0:-1]) + '_' + str(b) + '.bmp'
                    if not os.path.exists(filename):
                        # print(filename)
                        continue
                    size = os.path.getsize(filename)
                    if size < 500000:
                        continue
                    feature = lines[j].strip().split(' ')[1] + ' ' + lines[j].strip().split(' ')[2] + ' ' + \
                              lines[j].strip().split(' ')[3] + ' ' + lines[j].strip().split(' ')[4]
                    context = filename + ' ' + feature + '\n'
                    contexts.append(context)
                else:
                    b = b + 1
                    filename = '_'.join(lines[j].strip().split('_')[0:-1]) + '_' + str(b) + '.bmp'
                    if not os.path.exists(filename):
                        continue
                    size = os.path.getsize(filename)
                    if size < 500000:
                        continue
                    feature = lines[j].strip().split(' ')[1] + ' ' + lines[j].strip().split(' ')[2] + ' ' + \
                              lines[j].strip().split(' ')[3] + ' ' + lines[j].strip().split(' ')[4]
                    context = filename + ' ' + feature + '\n'
                    contexts.append(context)
                    # print(contexts)

        with open(a, 'w+') as fa:
            for z in contexts:
                fa.writelines(z)
            contexts = []
        print(a)
        # break


# txt文件批量处理
# 参数：txtpath = txt文件夹目录
def alterTxt():
    txtpath = './txt'

    txtlist = os.listdir(txtpath)
    lines = []
    for i in txtlist:
        lines = []
        filepath = os.path.join(txtpath, i)
        print(filepath)
        with open(filepath, 'r') as fb:
            for line in fb.readlines():
                line = line.replace('Z:\\datahome\\3d\\', './', 1)
                lines.append(line)
        with open(filepath, 'w') as fc:
            for line in lines:
                fc.writelines(line)


# K01据处理 按200服务器文件结构整理解析好的bmp数据，并保存186源数据域200服务器数据的对应关系表 -- 《186_200.txt》
# 注：输出单人编号的文件夹为7位数
# 参数：
#       picpath : 解析好的bmp文件源路径
#       outpath : 拷贝输出bmp文件路径
#       num ：单人路径起始编号
# 返回值：处理好的单人路径编号最后一个的后面一个
def collatingOfdata(bmppath, outpath, num):
    humanlist = os.listdir(bmppath)
    txtcontext = []
    for i in humanlist:
        target = str('%07d' % num)
        humanpath = os.path.join(bmppath, i)
        targetpath = os.path.join(outpath, target)
        txt = i + ' - ' + target + '\n'
        txtcontext.append(txt)
        if not os.path.exists(targetpath):
            os.makedirs(targetpath)

        aalsit = os.listdir(humanpath)
        if len(os.listdir(os.path.join(humanpath, aalsit[0]))) < 20:
            continue
        num += 1
        for j in aalsit:
            pictypepath = os.path.join(humanpath, j)

            command = 'cp -r ' + pictypepath + ' ' + targetpath

            os.system(command)
            print(command)
    with open('186_200_2.txt', 'a+') as fb:
        for z in txtcontext:
            fb.writelines(z)
    return num


# 3D数据处理 删除采集文件中的png目录
# 参数：3D采集目录
def delPng(inpath):
    # inpath = './20190711'

    inpathlist = os.listdir(inpath)
    for i in inpathlist:
        apath = os.path.join(inpath, i)
        for j in os.listdir(apath):
            if j != 'Png':
                # if j != 'dep':
                continue
            bpath = os.path.join(apath, j)
            command = 'rm -r ' + bpath
            os.system(command)
            print(command)


def rename(inpath):
    inpathlist = os.listdir(inpath)
    num = 150
    for i in sorted(inpathlist):
        apath = os.path.join(inpath, i)
        bpath = os.path.join(inpath, str(num) + '.bmp')
        num += 1
        command = 'mv ' + apath + ' ' + bpath
        os.system(command)
        print(command)


if __name__ == '__main__':
    num = collatingOfdata('W:\\datahome\\k01_datahome\\20190731_bmp_2', 'W:\\datahome\\k01_datahome\\20190731_data', 77)
    # rename('./color')
    # num = collatingOfdata('F:\\frames\\collating_jieyang_bmp', 'F:\\frames\\collating_bmp_data', 1284)
