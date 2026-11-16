import os
import shutil
from pathlib import Path

path="/home/elei/learning"
target_dir='/home/elei/back_up'
os.makedirs(target_dir,exist_ok=True)

for file_path,folders,files in os.walk(path):
        if 'l_venv' in folders:
            folders.remove('l_venv')
        if 'test.py' in files:
            source_file=os.path.join(file_path,'test.py')
            shutil.copy(source_file,target_dir)
            print('file copied.')

        

#纯pathlib
base_path=Path('./learning')
target_dir=Path('./back_up')
target_dir.mkdir(exist_ok=True)

for file in base_path.rglob('test.py'):
    if 'l_venv' in file.parts:
        continue
    shutil.copy(file,target_dir)
    print(f'ok,{file} is copied')
