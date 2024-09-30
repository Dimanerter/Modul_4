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
