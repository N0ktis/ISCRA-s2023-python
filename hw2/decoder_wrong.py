import math
import sys


def index_to_bytes(value, bits):
    n = bits // 8
    if bits % 8 != 0:
        n += 1
    return value.to_bytes(n, 'little')


def num_of_bytes_to_read(dict_len):
    bits = math.ceil(
        math.log2(dict_len)
    )  # кол-во бит для представления числа len(dictionary) в binary формате (чтобы уместилось)
    bytes = bits // 8  # кол-во байт (получаем из кол-ва бит)
    if bits % 8 != 0:
        bytes += 1
    return bytes


def bytes_to_index(bytes_str):
    index = int.from_bytes(bytes_str,
                           'little')  # переводим байт/байты в индекс
    return index


if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) >= 4:
        print('Usage: python', sys.argv[0], 'input_file')
        print(
            'На входе должно быть от 1 или 2 аргумента (не считая сам исполняемый файл .py)!'
        )
        exit(-1)

    with open(sys.argv[1], 'rb') as file:
        data = file.read()
    dictionary = {i: (i, ) for i in range(256)}
    sequence = list()
    nseq = list()

    outpath = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1] + '.dec'
    with open(outpath, 'wb') as file:
        i = 0
        while i < len(data):
            n = len(dictionary)
            bits = math.ceil(math.log2(n))
            Bytes = math.ceil(
                bits / 8
            )  # кол-во байт для считывания (в первый раз - 1, затем - 2 и т.д.)
            ind = bytes_to_index(
                data[i:i +
                     Bytes])  # индекс соответствующей байт. последовательности
            if ind == len(dictionary):
                nseq = sequence + sequence[-1:]
            else:
                nseq = sequence + list(dictionary[ind])
            file.write(bytes(nseq))
            dictionary[len(dictionary)] = tuple(sequence + nseq[-1:])
            i += Bytes
            seq = nseq.copy()
