def main():
    string = input()
    shift = int(input())
    print("".join(
        chr(ord('a') + (ord(char.lower()) - ord('a') + shift) % (ord('z') - ord('a') + 1)) for char in string
    ))


if __name__ == "__main__":
    main()
