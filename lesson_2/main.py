import math
import sys

def index_to_bytes(value, bits):
    n = bits // 8
    if bits % 8 != 0:
        n += 1
    return value.to_bytes(n, 'little')


if not (2 <= len(sys.argv) <= 3):
    print('Usage: python', sys.argv[0], 'input_file (output_file)')
    exit(-1)

with open(sys.argv[1], 'rb') as file:
    data = file.read()

dictionary = {(i,): i for i in range(256)}
sequence = list()

outpath = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1] + '.lzw'
# cond ? a : b
# a if cond else b
# if len(sys.argv) == 3:
#     outpath = sys.argv[2]
# else:
#     outpath = sys.argv[1] + '.lzw'
with open(outpath, 'wb') as file:
    for sym in data:
        sequence.append(sym)
        key = tuple(sequence)
        if key in dictionary:
            continue

        n = math.ceil(math.log2(len(dictionary)))
        index_value = dictionary[key[:-1]]
        enc_value = index_to_bytes(index_value, n)
        file.write(enc_value)

        value = len(dictionary)
        dictionary[key] = value
        # print(value, '->', key)

        sequence = sequence[-1:]

    n = math.ceil(math.log2(len(dictionary)))
    index_value = dictionary[tuple(sequence)]
    enc_value = index_to_bytes(index_value, n)
    file.write(enc_value)

        # [1, 2, 3]
        # [3]

        # a
        # a[b] -> [a] (ab) -> dict
        # b[e] -> [b] (be) -> dict
        # e

        # a
        # ab
        # ab[c] -> [ab] (abc) -> dict
