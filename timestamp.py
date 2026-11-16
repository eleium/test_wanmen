import os
import shutil
import time

base_path = "/home/elei/test/草蜢"
target_dir = "/home/elei/test/time"
os.makedirs(target_dir, exist_ok=True)

# target_dirs = {
#     "张宇": "/home/elei/test/张宇",
#     "林忆莲": "/home/elei/test/林忆莲",
#     "陈淑桦": "/home/elei/test/陈淑桦",
# }

# for t in target_dirs.values():
#     os.makedirs(t, exist_ok=True)

for filepath, folders, files in os.walk(base_path):
    # if "视频" in folders:
    #     folders.remove("视频")
    for file in files:
        # for key, value in target_dirs.items():
        #     if key in file:
        #         shutil.copy(os.path.join(filepath, file), os.path.join(value, file))
        #         print(f"{file} is copied")
        # size = os.path.getsize(os.path.join(filepath, file)) / 1024 / 1024
        # if size > 15:
        #     print(f"{file}, {size:.2f}M")

        # 获取时间戳
        timestamp = os.path.getmtime(os.path.join(filepath, file))
        print(timestamp)

        # 将机器时间换算成人类时间
        human_time = time.localtime(timestamp)
        print(human_time)
        # 将人类时间以下面的格式展现
        datetime = time.strftime("%Y-%m-%d %H:%M", human_time)
        print(datetime)

        # 设立比对时间
        target_time = "2026-11-14 21:00"
        # 按格式转化
        time_array = time.strptime(target_time, "%Y-%m-%d %H:%M")
        # 将这个比对时间转化为时间戳：
        my_target_time = float(time.mktime(time_array))

        if my_target_time < timestamp:
            shutil.copy(os.path.join(filepath, file), target_dir)
