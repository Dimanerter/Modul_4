from pathlib import Path, PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)
print("Suffix", p.suffix)
print("Parent:", p.parent)

