line = input()
while True:
    x, y = input().split('->')
    line = line.replace(x, y)
    print(line)
