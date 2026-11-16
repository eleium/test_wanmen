import shutil
from pathlib import Path

# 纯pathlib
base_path = Path("/home/elei/learning")
target_dir = Path("/home/elei/back_up")
target_dir.mkdir(exist_ok=True)

for file in base_path.rglob("test.py"):
    if "l_venv" in file.parts:
        continue
    shutil.copy(file, target_dir)
    print(f"ok,{file} is copied")
