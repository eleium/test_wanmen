import shutil
from pathlib import Path

base_dir = Path("/home/elei/music")

target_dirs = {
    "陈慧娴": Path("/home/elei/test/陈慧娴"),
    "王杰": Path("/home/elei/test/王杰"),
    "草蜢": Path("/home/elei/test/草蜢"),
}

for t in target_dirs.values():
    t.mkdir(exist_ok=True)

for name, target_dir in target_dirs.items():
    for file in base_dir.rglob(f"*{name}*.mp3"):
        # 🚨 正确逻辑：如果路径里包含"视频"，直接跳过这个文件
        if "视频" in file.parts:
            continue
        if file.is_file():
            size = file.stat().st_size / 1024 / 1024
            shutil.copy(file, target_dir)
            print(f"{file.name} is copied.")
            if size > 10:
                print(f"【大文件】{file.name} 已复制，大小: {size:.2f} MB")
