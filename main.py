from salary import total_salary
from cats import get_cats_info
from pathlib import Path
import subprocess
import sys


def run_salary():
    path = input("Path to salary file: ")
    total, avg = total_salary(path)
    print(f"Total: {total}, Average: {avg}")


def run_cats():
    path = input("Path to cats file: ")
    cats = get_cats_info(path)
    for cat in cats:
        print(cat)


def run_tree():
    path = input("Path to directory: ")
    subprocess.run([sys.executable, "hw03.py", path])


def run_assistant():
    subprocess.run([sys.executable, "assistant.py"])


def main():
    while True:
        print("\n=== goit-pycore-hw-04 ===")
        print("1 - Salary calculation")
        print("2 - Cats info")
        print("3 - Directory tree")
        print("4 - Assistant bot")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            run_salary()
        elif choice == "2":
            run_cats()
        elif choice == "3":
            run_tree()
        elif choice == "4":
            run_assistant()
        elif choice == "0":
            print("Good bye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()