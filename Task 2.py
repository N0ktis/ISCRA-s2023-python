s = input()
x = input().split("->")

while x:
    try:
        print(s.replace(x[0], x[1]))
    except:
        break
    x = input().split('->')
