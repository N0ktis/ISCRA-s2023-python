def main():
    string = input().replace(' ', '')
    shift = int(input())
    print("".join(chr((ord('a') + ((ord(char.lower()) + shift) % (ord('z') + 1)) % ord('a')) % 127) for char in string))


if __name__ == "__main__":
    main()

