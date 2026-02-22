import os

def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid file format")

    return cats


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "cats_file.txt")

    cats = get_cats_info(file_path)  # <-- обов'язково викликати

    for cat in cats:
        print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")
