import math
import sys


def index_to_bytes(value, bits):
    n = bits // 8
    if bits % 8 != 0:
        n += 1
    return value.to_bytes(n, 'little')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python', sys.argv[0], 'input_file')
        exit(-1)
    with open(sys.argv[1], 'rb') as file:
        data = file.read()
    dictionary = {(i,): i for i in range(256)}
    sequence = list()

    outpath = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1] + '.lzw'
    with open(outpath, 'wb') as file:
        for sym in data:
            sequence.append(sym)
            key = tuple(sequence)
            if key in dictionary:
                continue

            n = math.ceil(
                math.log2(len(dictionary)))  # кол-во бит для представления числа len(dictionary) в binary формате
            index_value = dictionary[key[:-1]]
            enc_value = index_to_bytes(index_value, n)
            file.write(enc_value)

            value = len(dictionary)
            dictionary[key] = value
            # print(value, '->', key)
            sequence = sequence[-1:]

        n = math.ceil(
            math.log2(len(dictionary)))  # кол-во бит для представления числа len(dictionary) в 2-ом формате
        index_value = dictionary[tuple(sequence)]
        enc_value = index_to_bytes(index_value, n)
        file.write(enc_value)
