s = input()
while True:
    old, new = input().split("->")
    s = s.replace(old, new)
    print(s)