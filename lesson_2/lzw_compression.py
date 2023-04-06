from math import ceil, log2
from sys import argv


def index_to_bytes(value: int, bits: int) -> bytes:
    return value.to_bytes((bits // 8) + (0 if bits % 8 == 0 else 1), "little")


def encode_value(dictionary: dict, key: tuple) -> bytes:
    return index_to_bytes(dictionary[key], ceil(log2(len(dictionary))))


def main(input_filename: str, output_filename: str) -> None:
    with open(input_filename, 'rb') as input_file:
        string_bitwise = input_file.read()

    with open(output_filename, 'wb') as output_file:
        dictionary = {(i,): i for i in range(256)}
        sequence = list()

        for char in string_bitwise:
            sequence.append(char)
            if (key := tuple(sequence)) in dictionary:
                continue

            output_file.write(encode_value(dictionary, key[:-1]))
            dictionary[key] = len(dictionary)
            sequence = sequence[-1:]
        output_file.write(encode_value(dictionary, tuple(sequence)))


if __name__ == "__main__":
    if not (2 <= len(argv) <= 3):
        print("Error: Wrong number of arguments.")
        print("Usage: python", argv[0], "input_file (output_file)")
        exit(-1)
    else:
        main(argv[1], argv[2] if len(argv) == 3 else argv[1] + ".lzw")
