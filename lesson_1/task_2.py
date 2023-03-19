def main():
    string = input()
    while True:
        if (rule := input()) != "end":
            print(string := string.replace((rule := rule.split("->"))[0], rule[1]))
        else:
            break


if __name__ == "__main__":
    main()
