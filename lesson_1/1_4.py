line = input()
numbers = line.split()
result = [float(num) for num in numbers]
powresult = [pow(res, 2) for res in result]
sumresult = [sum(powresult)]
print(sumresult)
