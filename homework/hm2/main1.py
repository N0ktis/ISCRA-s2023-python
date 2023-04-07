import math
import sys
dictionary = {i: (i,) for i in range(0, 256)}
working_arr = []
k = 0

if not (len(sys.argv) == 2):
    print('Usage: python', sys.argv[0], 'input_file')
    exit(-1)

with open(sys.argv[1] + "decoded", 'wb') as file:
    with open(sys.argv[1], 'rb') as file1:
        while True:
            n = math.ceil(math.log2(len(dictionary)))
            byte_amount = n // 8
            if k != 0:
                byte_amount += 1
            bytess = file1.read(byte_amount)
            if not bytess:
                break
            num = int.from_bytes(bytess, "little")
            if dictionary.get(num) != None:
                symbols = dictionary[num]
                working_arr.append(symbols[0])
                if (k != 0):
                    dictionary[len(dictionary)] = tuple(working_arr)
                k = 1
                file.write(bytes(list(symbols)))
                working_arr = list(symbols)
            else:
               working_arr.append(working_arr[0])
               file.write(bytes(working_arr))
               dictionary[len(dictionary)] = tuple(working_arr)