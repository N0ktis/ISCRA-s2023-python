def main():
    main_line = input()
    key = int(input())
    answer = []
    for i in main_line:
        answer.append((chr((ord(i) + key))))
    for i in answer:
        print(i, end = "")
if __name__== '__main__':
    main()