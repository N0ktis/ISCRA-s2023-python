import math
import sys

if not (2 <= len(sys.argv) <= 3):
    print('Usage: python', sys.argv[0], 'input_file')
    exit(-1)

with open(sys.argv[1],'rb') as file:
    data = file.read()

outpath = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1] + '.txt'
dictionary = {i: (i,) for i in range(256)}
sequence = list()
i = 0

with open(outpath, 'wb') as file:
    while i < len(data):
        if len(sequence) == 0:
            n = len(dictionary)
        else:
            n = len(dictionary) + 1
        nbits = math.ceil(math.log2(n))
        if nbits % 8 == 0:
            nbytes = nbits // 8
        else:
            nbytes = nbits // 8 + 1
        Slice = data[i:i + nbytes]
        index = int.from_bytes(Slice, 'little')
        if index == len(dictionary):
            new_sequence = sequence + sequence[-1:]
        else:
            new_sequence = list(dictionary[index])
        file.write(bytearray(new_sequence))
        dictionary[len(dictionary)] = tuple(sequence + new_sequence[-1:])
        i += nbytes
        sequence = new_sequence
