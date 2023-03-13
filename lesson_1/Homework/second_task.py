string = input()

while rule := input():
    print(string := string.replace(rule[0], rule[-1]))