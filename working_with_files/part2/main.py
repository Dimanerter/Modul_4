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

