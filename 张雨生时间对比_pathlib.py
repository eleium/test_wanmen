import os
import shutil
import time
from datetime import datetime
from pathlib import Path

source_dir = Path("~/music").expanduser()
target_dir = Path("/home/elei/test/周华健")
target_dir.mkdir(exist_ok=True)


# 设定对比时间(字符串)
target_time_str = "2020-10-3 13:30"


# 用pathlib方法：
target_dt = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M")
# strptime（p 代表 parse，解析）：字符串 -> 时间对象。你平时解析用户输入或读取文本时用。
# strftime（f 代表 format，格式化）：时间对象 -> 字符串。你想把时间打印得漂亮点给人看时用。


for song_file in source_dir.rglob("*周华健*"):
    if "videos" in song_file.parts:
        continue

    shutil.copy(song_file, target_dir)
    print(f"{song_file} is copied to {target_dir}.")

    song_dt = datetime.fromtimestamp(song_file.stat().st_mtime)

    if target_dt < song_dt:
        print(f"{song_file} 在比对时间{target_dt}之后修改。")


###pathlib的时间转换逻辑：把字符串弄成“时间对象” ➡️ 把文件的浮点数也弄成“时间对象” ➡️ 两个“时间对象”直接比大小。

target_time_str = "2026-11-15 20:30"
# datetime.strptime:把字符串的时间，转化成一个时间对象。可以直接比对大小。
target_dt = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M")

# 读取文件的stat()，取其中的st_mtime修改时间属性，用datetime转化成一个时间对象。
song_dt = datetime.fromtimestamp(song_file.stat().st_mtime)

# 最终比较 target_dt 和 song_dt 这个两个时间对象.


###用os来转换逻辑：把字符串弄成“时间元组” ➡️ 把元组弄成“浮点数” ➡️ 拿浮点数和文件的“浮点数”干架比大小。

# 比对的时间字符串
target_time_str = "2026-11-15 16:57"

# 1,time.strptime() 转出来的是一个 “时间元组（struct_time）”。本质上是一堆数字组成的结构体，给机器用来做中间转换用的。
# 它长得像这样：time.struct_time(tm_year=2026, tm_mon=11, tm_mday=15, tm_hour=16, tm_min=57, ...)。
target_time_tuple = time.strptime(target_time_str, "%Y-%m-%d %H:%M")
# 2,转成时间戳浮点数字:
target_timestamp = float(time.mktime(target_time_tuple))


# 文件修改时间的转化:

# 1,获取文件的时间戳,一串数字,可以与对比时间戳对比了.
file_timestamp = os.path.getmtime(os.path.join(filepath, file))
# 2,把时间戳转化为人类能看懂的时间元组,但是也不好看懂
file_time_tuple = time.localtime(file_timestamp)
# 3,将这个时间对象,按照指定的格式呈现,最符合人类的习惯.
file_time_str = time.strftime("%Y-%m-%d %H:%M", file_time_tuple)


# 最终对比的是:target_timestamp 和 file_timestamp


# 🎁 终极命名心法回顾（送你一个对照表）
# 变量名后缀	         代表的数据类型	                  典型值示例
# _str	                 字符串 (String)	              "2020-10-3 13:30"
# _tuple	             时间元组 (struct_time)	          time.struct_time(tm_year=2020...)
# _timestamp / _ts	     浮点数 (Float)	                  1601692200.0
# _dt	datetime         对象	                          datetime.datetime(2020, 10, 3, 13, 30)
# _path / _dir	         路径对象或字符串	              Path('/home/elei/music')

# 有了这套心法，以后不管是写 Python 还是转战 Go、Java，这种“带类型/带语义”的命名习惯，
# 都会让和你合作的人觉得你是个老手。你现在完全可以拿着这套模板，去随意收拾你电脑里的各种文件了！
