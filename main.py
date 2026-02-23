from salary import total_salary
from cats import get_cats_info
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_user_path(raw_path: str) -> str:
    candidate = Path(raw_path).expanduser()
    if candidate.is_absolute():
        return str(candidate)
    return str((BASE_DIR / candidate).resolve())


def run_salary():
    path = input("Path to salary file: ")
    path = resolve_user_path(path)
    total, avg = total_salary(path)
    print(f"Total: {total}, Average: {avg}")


def run_cats():
    path = input("Path to cats file: ")
    path = resolve_user_path(path)
    cats = get_cats_info(path)
    for cat in cats:
        print(cat)


def run_tree():
    path = input("Path to directory: ")
    path = resolve_user_path(path)
    script_path = BASE_DIR / "hw03.py"
    subprocess.run([sys.executable, str(script_path), path])


def run_assistant():
    script_path = BASE_DIR / "assistant.py"
    subprocess.run([sys.executable, str(script_path)])


def main():
    actions = {
        "1": run_salary,
        "2": run_cats,
        "3": run_tree,
        "4": run_assistant,
    }

    while True:
        print("\n=== goit-pycore-hw-04 ===")
        print("1 - Salary calculation")
        print("2 - Cats info")
        print("3 - Directory tree")
        print("4 - Assistant bot")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "0":
            print("Good bye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice")
            continue

        action()


if __name__ == "__main__":
    main()
