import os
import shutil

path='/home/elei/music'
target='/home/elei/test/liudehua'
os.makedirs(target,exist_ok=True)

for filepath,folders,files in os.walk(path):
    if '视频' in folders:
        folders.remove('视频')
    for file in files:
        if '刘德华' in file:
            shutil.copy(os.path.join(filepath,file),os.path.join(target,file))
            #shutil.copy(os.path.join(filepath,file),os.makedirs('/home/elei/test/liudehua',exist_ok=True))
            print(f'{file} is copied')
