string = input()
while True:
    cond = input()
    print(string.replace((input().split("->"))[0], (input().split("->"))[1]))
