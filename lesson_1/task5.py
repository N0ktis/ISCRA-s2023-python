def main():
    main_line = input().lower().replace(" ", "")
    key = int(input())
    answer = []
    for i in main_line:
        if ord(i) + key > 122:
            answer.append(chr(((ord(i) + key))%122 + 96))
        else:
            answer.append(chr((ord(i) + key)))
    for i in answer:
        print(i, end = "")
if __name__== '__main__':
    main()