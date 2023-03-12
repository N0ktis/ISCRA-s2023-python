string = input()

while True:
    ch, rep = (i for i in input().split('->'))
    string = string.replace(ch, rep)
    print(string)
