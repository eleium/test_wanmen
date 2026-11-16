import os
import shutil
import time

path = '/home/elei/music'
target_dir = '/home/elei/test/张雨生'
os.makedirs(target_dir, exist_ok=True)

# 提前算好目标时间
target_time = '2026-11-14 21:30'
format_time = time.strptime(target_time, '%Y-%m-%d %H:%M')
target_timestamp = time.mktime(format_time)

for filepath, folders, files in os.walk(path):
    if '视频' in folders:
        folders.remove('视频')

    for file in files:
        # 1. 只要张雨生的歌
        if '张雨生' in file:
            full_path = os.path.join(filepath, file)
            
            # 2. 复制过去
            shutil.copy(full_path, target_dir)
            
            # 3. 获取时间并比对
            timestamp = os.path.getmtime(full_path)
            human_time = time.localtime(timestamp)
            formate_dt = time.strftime('%Y-%m-%d %H:%M', human_time)
            
            # 打印一下这首歌的时间（让你看得见）
            print(f"已复制：{file} | 修改时间：{formate_dt}")
            
            # 4. 如果时间早于目标时间（注意符号是 < ）
            if timestamp < target_timestamp:
                print(f"   👉 【符合条件的老歌】: {file}")
