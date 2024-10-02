from pathlib import Path
import time

# Створення об'єкту Path для директорії
directory = Path("./picture")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)


directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)

directory = Path('/my_directory/new_folder')
directory.rmdir()

path = Path("./picture")

# Перевірка існування
if path.exists():
    print(f"{path} існує")

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

file_path = Path("./picture/bot-icon.png")

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")

file_path = Path("./picture/bot-icon.png")

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')
