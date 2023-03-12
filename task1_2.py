import sys

line = input()
while True:
    a, b = input().split('->')
    line = line.replace(a, b)
    print(line)
