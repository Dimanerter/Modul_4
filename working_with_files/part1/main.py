fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    # print(symbol)

fh.close()

#-----------------------------readline-------------------------------

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()


fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.seek(0)
lines = [el.strip() for el in fh.readlines()]
print(lines)
fh.close()

#-----------------------------seek and tell-------------------------------

fh = open('test.txt', 'w+')
fh.write("hello!")
position = fh.tell()
print(position)

fh.seek(1)
position = fh.tell()
print(position)

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()

#-----------------------------Менеджер контексту-------------------------------

# fh = open('test.txt', 'w')
# try:
#     fh.write('Some data')
# finally:
#     fh.close()

# with
with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)

#-----------------------------Робота з не текстовими файлами у Python-------------------------------

with open('raw_date.bin', 'wb') as fh:
    fh.write(b'Hello world!')


s = b'Hello!'
print(s[1])

byte_str = 'some text'.encode()
print(byte_str)


# Перетворення чисел у байт-рядки

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)

for num in [127, 255,156]:
    print(hex(num))


# Кодування рядків (ASCII, UTF-8, CP1251)

# print(ord('%'))
# print(chr(1000))

# s = "Привіт!"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode('utf-16')
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode('cp1251')
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)


# print(b'Hello world!'.decode('utf-16'))

with open('test.txt','r', encoding = 'utf-8') as file:
    content = file.read()
    print(content)

# Масив байтів

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)


byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))
print(byte_array)

byte_array = bytearray(b"Hello world!")
string = byte_array.decode("utf-8")
print(string)

