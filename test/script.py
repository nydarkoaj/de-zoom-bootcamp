from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"{current_dir}/{current_file}")


for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f" - {filepath.name}")