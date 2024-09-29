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
lines = fh.readlines()
print(lines)


fh.close()

