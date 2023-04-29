import math
import sys

if not (2 <= len(sys.argv) <= 3):
    print('Usage: python', sys.argv[0], '{encoded_file}.lwz (output_file)')
    exit(-1)

in_path = sys.argv[1]

out_path = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1][:-4][:sys.argv[1][:-4].find('.')] + '_dec' \
                                                  + sys.argv[1][:-4][sys.argv[1][:-4].find('.'):]

dictionary = {i: (i,) for i in range(256)}

current_bytes = []

with open(in_path, 'rb') as file_in:
    with open(out_path, 'wb') as file_out:
        bites = math.ceil(math.log2(len(dictionary)))
        bytes = bites // 8
        if bytes % 8 == 0:
            bytes += 1
        sym = int.from_bytes(file_in.read(bytes), byteorder='little')
        file_out.write(bytearray(dictionary[sym]))
        current_bytes.append(dictionary[sym][0])
        current_bytes.append(sym)
        current_bytes = list(dictionary[sym])
        while(True):
            bites = math.ceil(math.log2(len(dictionary)))
            bytes1 = bites // 8
            bytes1 += 1
            sym = file_in.read(bytes1)
            if not sym:
                break
            sym = int.from_bytes(sym, byteorder='little')
            #print('byte array:', current_bytes)
            #print('int symbol:', sym)
            if sym in dictionary:
                file_out.write(bytearray(dictionary[sym]))
                current_bytes.append(dictionary[sym][0])
                dictionary[len(dictionary)] = tuple(current_bytes)
                current_bytes = list(dictionary[sym])
            else:
                current_bytes.append(current_bytes[0])
                file_out.write(bytearray(current_bytes))
                dictionary[len(dictionary)] = tuple(current_bytes)
            #print('=====================')

print('new entries in the dictionary:')
printable_key = []
for i in range(256, len(dictionary)):
    for j in range(len(dictionary[i])):
        printable_key.append(chr(dictionary[i][j]))
    print(i, '->', ''.join(printable_key))
    printable_key.clear()