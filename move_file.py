import shutil
from pathlib import Path


def move_file(source_dir: Path, target_dir: Path):
    target_dir.mkdir(parents=True, exist_ok=True)
    for file in source_dir.rglob("*.py"):
        if file.resolve() == Path(__file__).resolve():
            continue

        if not file.is_file():
            continue

        check_file = target_dir / file.name
        if check_file.exists():
            continue

        shutil.move(str(file), str(check_file))
        print(f"{file.name} is moved to {target_dir}.")


if __name__ == "__main__":
    source_dir = Path("/home/elei/test")
    target_dir = Path("/home/elei/learning")
    move_file(source_dir, target_dir)
