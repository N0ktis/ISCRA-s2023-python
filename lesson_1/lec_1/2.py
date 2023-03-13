# 2 task

line = input()
while True:
    cond = input().split('->')
    line = line.replace(cond[0], cond[1])
    print(line)
