import sys
import math
def main():
    main_line = input()
    print(main_line)
    while True:
        parts = input()
        if parts == "":
            break
        parts = parts.split("->")
        s = main_line.replace(parts[0], parts[1])
        main_line = s
        print(s)

if __name__== '__main__':
    main()