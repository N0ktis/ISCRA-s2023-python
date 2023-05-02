import math
import sys


def amount_bytes(bits):
    n = bits // 8
    if bits % 8 != 0:
        n += 1
    return n


if len(sys.argv) != 2:
    print('Usage: python', sys.argv[0], 'input_file (output_file)')
    exit(-1)

path = sys.argv[1]
outpath = sys.argv[1][:-4] + ".txt"

with open(path, "rb") as file:
    data = file.read()

dictionary = {i: [i] for i in range(256)}
pair = list()
num = math.ceil(math.log2(len(dictionary)))
num = amount_bytes(num)
sym_a = b""
first_el = True
byte_num= 0
with open(outpath, 'wb') as file:
    while byte_num< len(data):
        if first_el:
            pair.append(list(dictionary[data[byte_num]]))
            first_el = False
            num = 2
            byte_num+= 1
            continue
        if num > 0:
            sym_a += data[byte_num].to_bytes(1, "little")
            num -= 1
            byte_num+= 1
            continue
        pair.append(list())
        print(len(dictionary))
        for j in dictionary[int.from_bytes(sym_a, "little")]:
            pair[1].append(j)
        dictionary[len(dictionary)] = list()
        sym_a = b""
        for i in pair[0]:
            for j in dictionary[i]:
                dictionary[len(dictionary) - 1].append(j)
        dictionary[len(dictionary) - 1].append((dictionary[pair[1][0]][0]))
        num = math.ceil(math.log2(len(dictionary)))
        num = amount_bytes(num)
        for i in pair[0]:
            for j in dictionary[i]:
                file.write(j.to_bytes(1, "little"))
        pair = pair[1:]

    pair.append(list())
    for j in dictionary[int.from_bytes(sym_a, "little")]:
        pair[1].append(j)
    dictionary[len(dictionary)] = list()
    sym_a = b""
    for i in pair[0]:
        for j in dictionary[i]:
            dictionary[len(dictionary) - 1].append(j)
    dictionary[len(dictionary) - 1].append((dictionary[pair[1][0]][0]))
    num = math.ceil(math.log2(len(dictionary)))
    num = amount_bytes(num)
    for i in pair:
        for z in i:
            for j in dictionary[z]:
                file.write(j.to_bytes(1, "little"))
for e in dictionary:
    if e > 255:
        print(dictionary[e], "->", e)
