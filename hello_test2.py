import os
import shutil

path = "/home/elei/learning"
target_dir = "/home/elei/back_up"
os.makedirs(target_dir, exist_ok=True)

for filepath, folders, files in os.walk(path):
    if "test.py" in files:
        source_file = os.path.join(filepath, "test.py")
        shutil.copy(source_file, target_dir)
        print("ok")
