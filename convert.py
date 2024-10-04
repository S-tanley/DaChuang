import cv2
import os

def read_path(file_pathname):
    n = 0
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        #####save figure
        cv2.imwrite("/Users/zhengbowen/nondefault/DaChuang_local/output_video/213c/"+"213"+str(n)+".png", img) 
        n += 1    

# 注意*处如果包含家目录（home）不能写成~符号代替 
# 必须要写成"/home"的格式，否则会报错说找不到对应的目录
# 读取的目录
read_path("/Users/zhengbowen/nondefault/DaChuang_local/output_video/213")
# print(os.getcwd())
