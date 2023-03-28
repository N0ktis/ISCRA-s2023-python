import math
import sys

if not (2 <= len(sys.argv) <= 3):
    print('Usage: python', sys.argv[0], 'input_file')
    exit(-1)

with open(sys.argv[1],'rb') as file:
    data = file.read()

outpath = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1] + '.unlzw'
dictionary = {i: (i,) for i in range(256)}
sequence = list()
i = 0
with open(outpath, 'wb') as file:
    while i < len(data):
        if len(sequence) == 0:
            n = len(dictionary)
        else:
            n = len(dictionary) + 1
        bits = math.ceil(math.log2(n))
        bytes = math.ceil(bits / 8)
        slice = data[i:i + bytes]
        index = int.from_bytes(slice, 'little')
        if index == len(dictionary):
            new_sequence = sequence + sequence[-1:]
        else:
            new_sequence = list(dictionary[index])
        file.write(bytearray(new_sequence))
        dictionary[len(dictionary)] = tuple(sequence + new_sequence[-1:])
        i += bytes
        sequence = new_sequence

