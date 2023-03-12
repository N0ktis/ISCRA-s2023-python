line = input()
massive = [x**2 for x in map(float,line.split())]
print(sum(massive))