import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def show_tree(path: Path, prefix=""):
    items = list(path.iterdir())
    for index, item in enumerate(items):
        is_last = index == len(items) - 1

        branch = "└── " if is_last else "├── "
        new_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            print(f"{prefix}{branch}{Fore.BLUE}{item.name}/")
            show_tree(item, new_prefix)
        else:
            print(f"{prefix}{branch}{Fore.GREEN}{item.name}")

def main():
    if len(sys.argv) < 2:
        print("❌ Path not provided")
        return

    path = Path(sys.argv[1])

    if not path.exists() or not path.is_dir():
        print("❌ Invalid directory path")
        return

    print(f"{Fore.BLUE}{path.name}/")
    show_tree(path)

if __name__ == "__main__":
    main()