import math
import sys

if not (2 <= len(sys.argv) <= 3):
    print('Usage: python3', sys.argv[0], '[file for decoding] (name of new file)')
    exit(-1)

with open(sys.argv[1], 'rb') as file:
    data = file.read()

dictionary = {i: (i,) for i in range(256)}

sequence = list()
count = 0
outpath = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1] + '.dec'
with open(outpath, 'wb') as file:
    while count < len(data):
        if len(sequence) == 0:
            n = len(dictionary)
        else:
            n = len(dictionary) + 1

        quantity_bits = math.ceil(math.log2(n))
        quantity_bytes = math.ceil(quantity_bits / 8)

        data_slice = data[count:count + quantity_bytes]
        index = int.from_bytes(data_slice, 'little')
        if index == len(dictionary):
            new_sequence = sequence + sequence[-1:]
        else:
            new_sequence = list(dictionary[index])

        file.write(bytearray(new_sequence))

        dictionary[len(dictionary)] = tuple(sequence + new_sequence[-1:])
        count = count + quantity_bytes
        sequence = new_sequence
