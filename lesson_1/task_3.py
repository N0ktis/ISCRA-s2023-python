def main():
    string = input()
    print(" ".join(number.split('.')[0][1 if number[0] == '-' else 0:] for number in string.split(" ")))


if __name__ == "__main__":
    main()
