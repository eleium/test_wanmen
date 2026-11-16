import os
import shutil

path='/home/elei/music'
target1='/home/elei/test/谭咏麟'
target2='/home/elei/test/张国荣'
os.makedirs(target1,exist_ok=True)
os.makedirs(target2,exist_ok=True)

for filepath,folders,files in os.walk(path):
    if 'videos' in folders:
        folders.remove('videos')
    for file in files:
        if '谭咏麟' in file:
            shutil.copy(os.path.join(filepath,file),target1)
            print(f'{file} is copied.')
        elif '张国荣' in file:
            shutil.copy(os.path.join(filepath,file),target2)
            print(f'{file} is copied in {target2}')

        elif '罗大佑' in file:
            if os.path.exists('/home/elei/test/罗大佑'):
                shutil.copy(os.path.join(filepath,file),'/home/elei/test/罗大佑')
            else:
                os.makedirs('/home/elei/test/罗大佑',exist_ok=True)
                shutil.copy(os.path.join(filepath,file),'/home/elei/test/罗大佑')
            print(f'{file} is copied')


from pathlib import Path

path=Path('/home/elei/music')
target_dir=Path('/home/elei/test/苏芮')
target_dir.mkdir(exist_ok=True)

for file in path.rglob('*苏芮*'):
    shutil.copy(file,target_dir)
    print(f'yes,{file} is copied in {target_dir}')
