import shutil
from pathlib import Path

path = Path("/home/elei/music")

artists = {
    "蔡琴": Path("/home/elei/test/蔡琴"),
    "刘鸿": Path("/home/elei/test/刘鸿"),
    "崔健": Path("/home/elei/test/崔健"),
}


for name, target_path in artists.items():
    target_path.mkdir(exist_ok=True)

    for file in path.rglob(f"*{name}*.mp3"):
        shutil.copy(file, target_path)
        print(f"{name} is copied in {target_path}")

        # size=os.path.getsize(file)/1024/1024
        size = file.stat().st_size / 1024 / 1024
        if size > 1:
            print(size)
