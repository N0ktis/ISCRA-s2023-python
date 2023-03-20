import re
line = input()
while True:
    rule = input()
    a,b = (remov for remov in rule.split('->'))
    line = line.replace(a,b)
    print(line)