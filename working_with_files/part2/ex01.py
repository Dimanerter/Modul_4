from pathlib import Path

# Створення об'єкту Path для директорії
directory = Path("./picture")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)
