string = input()
while True:
    ch, nch = input().split("->")
    string = string.replace(ch, nch)
    print(string)
