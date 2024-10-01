from pathlib import Path, PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)
print("Suffix", p.suffix)
print("Parent:", p.parent)

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 


base_path = Path("/usr/bin")

full_path = base_path / "subdir" / "script.py"

print(full_path)

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

original_path = Path("documents/example.txt")

new_path = original_path.with_name("report.txt")
print(new_path)

original_path = Path("documents/example.txt")
new_path = original_path.with_suffix(".md")
print(new_path)

print(original_path)

# original_path = Path("C:/Users/avdee/Documents/example.txt")

# new_path = original_path.with_name("report.txt")
# original_path.rename(new_path)


# -------------------------------Читання та запис файлів--------------------
file_path = Path("example.txt")

file_path.write_text("Привіт світ!", encoding = "utf-8")











