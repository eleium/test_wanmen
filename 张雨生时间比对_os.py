import os
import shutil
import time

path = "/home/elei/music"
target_dir = "/home/elei/test/张雨生"
os.makedirs(target_dir, exist_ok=True)


target_time = "2026-11-14 21:30"
format_time = time.strptime(target_time, "%Y-%m-%d %H:%M")
target_timestamp = float(time.mktime(format_time))

for filepath, folders, files in os.walk(path):
    if "视频" in folders:
        folders.remove("视频")

    for file in files:
        if "张雨生" in file:
            shutil.copy(os.path.join(filepath, file), target_dir)
            print(f"{file} is copied to {target_dir}")

            # 循环内，适合歌曲数量多。但是不容易查错。
            # timestamp = os.path.getmtime(os.path.join(filepath, file))
            # human_time = time.localtime(timestamp)
            # formate_dt = time.strftime("%Y-%m-%d %H:%M", human_time)
            # print(formate_dt)

            # if timestamp > target_timestamp:
            #     print(f"{file} 比 target_time 更新,是后来修改的。")

# 循环外，分工明确，但是啰嗦。适合歌曲数量少，因为要两次扫描磁盘。
for filepath1, folders1, files1 in os.walk(target_dir):
    for file1 in files1:
        timestamp = os.path.getmtime(os.path.join(filepath1, file1))
        human_time = time.localtime(timestamp)
        formate_dt = time.strftime("%Y-%m-%d %H:%M", human_time)
        print(formate_dt)

        if timestamp > target_timestamp:
            print(f"{file1} 比 target_time 更新,是后来修改的。")
