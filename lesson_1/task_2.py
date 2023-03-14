line = input()
while True:
    newSymbol = input()
    print(line.replace(newSymbol.split()[0], newSymbol.split()[2]))