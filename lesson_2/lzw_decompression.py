from sys import argv


def increase_sequence_len(old_len: int) -> tuple[int, int]:
    return (new_len := old_len + 1), pow(2, 8 * new_len)


def byte_sequence_append(sequence: bytes, symbol: int) -> bytes:
    return sequence + symbol.to_bytes(1, 'little')


def main(input_filename: str, output_filename: str) -> None:
    data = list[int]()
    with open(input_filename, 'rb') as input_file:
        sequence_len, max_dictionary_len = increase_sequence_len(1)
        data.append(int.from_bytes(input_file.read(1), 'little'))
        while len(byte_list := input_file.read(sequence_len)) == sequence_len:
            data.append(int.from_bytes(byte_list, 'little'))
            if data[-1] >= max_dictionary_len:
                sequence_len, max_dictionary_len = increase_sequence_len(sequence_len)

    with open(output_filename, 'wb') as output_file:
        dictionary = {i: i.to_bytes(1, 'little') for i in range(256)}
        output_file.write(sequence := dictionary[data[0]])
        for key in data[1:]:
            try:
                curr_sequence = dictionary[key]
            except KeyError:
                curr_sequence = byte_sequence_append(sequence, sequence[0])
            finally:
                dictionary[len(dictionary)] = byte_sequence_append(sequence, curr_sequence[0])
                output_file.write(sequence := curr_sequence)


if __name__ == "__main__":
    if not (2 <= len(argv) <= 3):
        print("Error: Wrong number of arguments.")
        print("Usage: python", argv[0], "input_file (output_file)")
        exit(-1)
    else:
        main(argv[1], argv[2] if len(argv) == 3 else argv[1] + ".decoded")
