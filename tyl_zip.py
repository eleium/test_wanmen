import os
import time
import zipfile 

source_dir='/home/elei/test/谭咏麟'
target_dir='/home/elei/test/zip_folder'

def zip_f():

    #更保险的方法，全部写入with,就不需要后面的close()了。
    with (zipfile.ZipFile(os.path.join(target_dir,'tyl.zip'),'w') as z,
          open(os.path.join(target_dir,'tyl.txt'),'w',encoding='utf-8') as w,):
        
    #z=zipfile.ZipFile(os.path.join(target_dir,'tyl.zip'),'w')
    #with open(os.path.join(target_dir,'tyl.txt'),'w',encoding='utf-8') as w:
        for file in os.listdir(source_dir):
            file_path=os.path.join(source_dir,file)
            if os.path.isfile(file_path):
                z.write(file_path,arcname=file)
                w.write(file+'\n')
    #z.close()
zip_f()



