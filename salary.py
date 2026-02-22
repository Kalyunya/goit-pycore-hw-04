import os

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    except ValueError:
        print("Invalid file format")
        return 0, 0

    average = total // count if count else 0
    return total, average


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "salary.txt")

    total, average = total_salary(file_path)
    print(f"Total salary: {total}")
    print(f"Average salary: {average}")