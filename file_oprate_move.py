"""将原文件夹的符合条件的文件,移动到目标文件夹"""

import shutil
import time
from pathlib import Path


def mv_file(source_dir, target_new_dir, target_old_dir, target_time_str):
    target_new_dir.mkdir(parents=True, exist_ok=True)
    target_old_dir.mkdir(parents=True, exist_ok=True)

    target_timestamp = time.mktime(time.strptime(target_time_str, "%Y-%m-%d %H:%M"))

    for file in source_dir.rglob("*.py"):
        # 保护脚本自身：如果当前遍历到的文件就是自己，直接跳过

        """__file__:这是 Python 运行脚本时自动生成的一个内置变量。
        它代表了当前正在运行的脚本文件的名字/路径（比如就是这个 mv_file.py)。
        Path(__file__)：把上面那个字符串路径变成一个 pathlib.Path 对象，方便后续处理。
        .resolve()：“刨根问底”解析成绝对路径。它会消除路径里的 ./、../，如果遇到软链接（快捷方式），
        它还会顺藤摸瓜找到真实文件。最终得到一个极其精确的、在硬盘上的真实绝对路径。
        结论:Path(__file__).resolve() 永远死死锁定“我（正在运行的代码）”在这个世界上的物理坐标。
        同理,file.resolve()就是遍历到的这个文件的真正绝对路径"""

        if file.resolve() == Path(__file__).resolve():
            continue

        # 剔除不想移动的文件:
        if any(
            part in file.parts
            for part in ("t_venv", "venv", ".venv", "env", "site-packages")
        ):
            continue

        # 检查当前遍历出来的path对象,是否是一个文件:
        if not file.is_file():
            continue

        # 查看当前遍历出来的文件的时间戳:
        file_timestamp = file.stat().st_mtime

        if file_timestamp > target_timestamp:
            # 检查目标文件夹是否有同名文件,如果有,就跳过,如果没有就continue->move
            dest = target_new_dir / file.name
            # 定义一个dest是为了方便,否则就是: if not (target_new_dir/file.name).exists():
            if not dest.exists():
                shutil.move(file, dest)
        else:
            dest = target_old_dir / file.name
            if not dest.exists():
                shutil.move(file, dest)


if __name__ == "__main__":
    source_dir = Path("/home/elei/test")
    target_new_dir = Path("/home/elei/learning/new_move")
    target_old_dir = Path("/home/elei/learning/old_move")
    target_time_str = "2026-11-18 20:30"

    mv_file(source_dir, target_new_dir, target_old_dir, target_time_str)
