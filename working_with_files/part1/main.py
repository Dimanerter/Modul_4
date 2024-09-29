

fh = open('test.txt', 'w+')

# symbols_written = fh.write('hello!')
fh.write('hello!')
fh.seek(0)
# print(symbols_written)
first_two_symbels = fh.read(2)
print(first_two_symbels)

fh.close()
