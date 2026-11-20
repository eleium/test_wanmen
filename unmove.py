import shutil
from pathlib import Path

# 假设你刚刚把文件移到了这里
current_dir = Path("/home/elei/learning")
# 你需要把它们放回原来的虚拟环境或库目录，比如你截图里的 t_venv
original_dir = Path(
    "/home/elei/test/t_venv/lib/python3.12/site-packages/requests"
)  # 路径需要你根据实际情况改


def undo_move():
    for file in current_dir.rglob("*.py"):
        target = original_dir / file.name
        # 如果原位置没有这个文件，就移回去
        if not target.exists():
            shutil.move(str(file), str(target))
            print(f"已恢复: {file.name}")


# 运行前一定要确认 original_dir 是对的！
# undo_move()
