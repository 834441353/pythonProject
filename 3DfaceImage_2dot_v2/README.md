## 使用环境：  
1. python3.6
2. PyQt5
3. tensorflow
4. opencv-python == 3.3.1.11
  
## 操作说明：
###### 1.  运行：  
`python ImageManage_main.py`
###### 2.  加载文件夹
1.  填写facepath和txtpath输入框  
    facepath：为需要处理的文件夹目录  
    facepath文件夹目录内部结构为：  
    ```
    source
    +-- folder1 +-- folder2 +--pic.jpg
    |           |           |--pic.jpg
    |           |           +--...
    |           |
    |           +-- folder2 +--pic.jpg
    |           |           |--pic.jpg
    |           |           +--...
    |           |
    |           +-- ...
    |
    +-- folder1 +-- folder2 +--pic.jpg
    |           |           |--pic.jpg
    |           |           +--...
    |           |
    |           +-- folder2 +--pic.jpg
    |           |           |--pic.jpg
    |           |           +--...
    |           |
    |           +-- ...
    +-- ...
    ```
    txtpath：为txt坐标文件保存的位置
    
2.  点击`加载文件夹`
3.  点击`开始`
###### 3.  标注  
1.  `修改`按钮：标注单张图片   
    **鼠标左键**：标注单个点
    **鼠标右键**：从已经标注的点中，依次从最后一个点开始删除  
    **鼠标左键双击标注点**：删除选中的标注点  
    **键盘q键**：关闭当前标注窗口（q键为英文输入法中的q键）  
    
2.  `跳过`按钮：跳过当前界面中显示的图片（不会再txt左边文件中记录）  
3.  `下一张`按钮：保存当前图片的坐标文件（内存中），在处理完单个***folder1***时才会储存在txt文件中  