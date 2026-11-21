import shutil
import time
from pathlib import Path

# 脚本目的：
# 1,将原文件夹的.py文件，按照修改时间、大小移动到目标文件夹
# 2,将已经移动到目标文件夹的文件，压缩打包。

source_dir = Path("/home/elei/test")

# ，把源文件夹里面的文件，按照修改时间，存入目标文件夹的两个文件夹下：


def mv_file(source_dir, target_new_dir, target_old_dir):
    target_new_dir.mkdir(exist_ok=True, parents=True)
    target_old_dir.mkdir(parents=True, exist_ok=True)

    target_time = "2026-11-18 20:30"
    # strptime 解析字符串 -> 时间元组；mktime 转为时间戳三部曲
    target_time_timestamp = time.mktime(time.strptime(target_time, "%Y-%m-%d %H:%M"))

    for file in source_dir.rglob("*.py"):
        # “随便找找看，在这个文件的路径（file.parts）里，有没有出现黑名单里的任何一个名字？
        # 如果有，就返回 True（触发 continue 跳过）。
        if any(
            part in file.parts
            for part in ("t_venv", ".venv", "venv", "env", "site-packages")
        ):
            # any() 会接收一个可迭代对象，上面是一个生成器。只要里面有任何一个元素是 True，就返回 True。
            continue
        if not file.is_file():
            continue

        #  2. 获取文件的最后修改时间戳
        file_time_timestamp = file.stat().st_mtime
        if file_time_timestamp > target_time_timestamp:
            dest = target_new_dir / file.name
            if not dest.exists():
                shutil.copy2(file, dest)
        else:
            dest = target_old_dir / file.name
            if not dest.exists():
                shutil.copy2(file, dest)


if __name__ == "__main__":
    target_new_dir = Path("/home/elei/learning/new_file")
    target_old_dir = Path("/home/elei/learning/old_file")

    mv_file(source_dir, target_new_dir, target_old_dir)

"""遍历穿透源文件后:
    1,先过滤不想执行的文件,比如虚拟环境。if not-->continue
    2,检查是否是文件夹。if not-->continue
    3,检查在目标文件夹里,是否有同名文件已经存在。if not -->shutil.copy2()
    4,对比时间的时间戳用三部曲法： target_timestamp=time.mktime(time.strptime,'%Y-%m-%d %H:%M')
    5,当前文件的时间戳： file_timestamp=file.stat().st_mtime

"""
