from os import walk,makedirs
import shutil
from pathlib import Path

path='/home/elei/music'

for filepath,folders,files in walk(path):
    print(folders)
    if 'videos' in folders:
        folders.remove('videos')
    for file in files:
        if '刘德华' in file:
            #file=os.path.join(filepath,'刘德华')
            shutil.copy(file,makedirs('/home/elei/back_up/liudehua'))
            print('ok')
                      
