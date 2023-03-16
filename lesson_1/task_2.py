def main():
    string = input()
    while True:
        if (rule := input()) != "end":
            old, new = rule.split("->")
            print(string := string.replace(old, new))
        else:
            break


if __name__ == "__main__":
    main()
