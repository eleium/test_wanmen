import os
import shutil

base_path = "/home/elei/music"

target_dirs = {
    "张宇": "/home/elei/test/张宇",
    "林忆莲": "/home/elei/test/林忆莲",
    "陈淑桦": "/home/elei/test/陈淑桦",
}

for t in target_dirs.values():
    os.makedirs(t, exist_ok=True)

for filepath, folders, files in os.walk(base_path):
    if "视频" in folders:
        folders.remove("视频")
    for file in files:
        for key, value in target_dirs.items():
            if key in file:
                shutil.copy(os.path.join(filepath, file), os.path.join(value, file))
                print(f"{file} is copied")
        size = os.path.getsize(os.path.join(filepath, file)) / 1024 / 1024
        if size > 15:
            print(f"{file}, {size:.2f}M")
