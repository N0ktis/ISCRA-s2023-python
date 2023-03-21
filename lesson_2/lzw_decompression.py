from sys import argv


def main(input_filename: str, output_filename: str) -> None:
    return None


if __name__ == "__main__":
    if not (2 <= len(argv) <= 3):
        print("Error: Wrong number of arguments.")
        print("Usage: python", argv[0], "input_file (output_file)")
        exit(-1)
    else:
        main(argv[1], argv[2] if len(argv) == 3 else argv[1] + ".decoded")
