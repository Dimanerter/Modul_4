from pathlib import Path, PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)
print("Suffix", p.suffix)
print("Parent:", p.parent)

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 