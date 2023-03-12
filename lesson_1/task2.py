string = input()
while True:
    a,b = input().split('->')
    string = string.replace(a,b)
    print(string)

