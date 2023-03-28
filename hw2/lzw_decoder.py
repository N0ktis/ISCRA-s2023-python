import math
from sys import argv

if len(argv) == 1:
    print('Usage: python ' + argv[0] + ' inp_file [out_file]')
    exit(-1)

with open(argv[1], 'rb') as inp_file:
    enc_str = inp_file.read()

byte_cnt = 0
dictionary = {i: [i] for i in range(256)}
out = b''

with open(argv[2] if len(argv) == 3 else argv[1][:-4], 'wb') as out_file:
    cur_str, cur_sl = dictionary[enc_str[0]], 0
    out_file.write(bytes(cur_str))
    prev_str = cur_str
    for entry in enc_str[1:]:
        byte_cnt += 1
        cur_sl = cur_sl + entry * 256 ** (byte_cnt - 1)
        if byte_cnt < math.ceil(math.log2(len(dictionary) + 1) / 8):
            continue
        byte_cnt = 0
        try:
            dictionary[cur_sl]
        except KeyError:
            dictionary[len(dictionary)] = prev_str + [prev_str[0]]
        cur_str, cur_sl = dictionary[cur_sl], 0
        out_file.write(bytes(cur_str))
        if prev_str + cur_str[:1] not in dictionary.values():
            dictionary[len(dictionary)] = prev_str + cur_str[:1]
        prev_str = cur_str
