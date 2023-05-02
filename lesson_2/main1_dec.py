import sys
import math


if not (2 <= len(sys.argv) <= 3):
    print('Usage: python', sys.argv[0], 'input_file (output_file)')
    exit(-1)

dictionary = {i: (i,) for i in range(256)}

inpath = sys.argv[1]
outpath = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1][:-4][:sys.argv[1].find('.')] + '_dec' + \
                                                sys.argv[1][:-4][sys.argv[1].find('.'):]

sequence = []

with open(inpath, 'rb') as file_in:
    with open(outpath, 'wb') as file_out:
        bites = math.ceil(math.log2(len(dictionary)))
        bytes = bites // 8
        if bytes % 8 == 0:
            bytes += 1
        data = file_in.read(bytes)
        sym = int.from_bytes(data, 'little')
        file_out.write(bytearray(dictionary[sym]))
        sequence.append(dictionary[sym][0])
        sequence.append(sym)
        sequence = list(dictionary[sym])
        while True:
            bites = math.ceil(math.log2(len(dictionary)))
            bytes_in_cycle = bites // 8
            bytes_in_cycle += 1
            sym = file_in.read(bytes_in_cycle)
            if not sym:
                break
            sym = int.from_bytes(sym, 'little')
            if sym in dictionary:
                file_out.write(bytearray(dictionary[sym]))
                sequence.append(dictionary[sym][0])
                dictionary[len(dictionary)] = tuple(sequence)
                sequence = list(dictionary[sym])
            else:
                sequence.append(sequence[0])
                file_out.write(bytearray(sequence))
                dictionary[len(dictionary)] = tuple(sequence)