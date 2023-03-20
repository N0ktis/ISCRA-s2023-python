line = input()
numbers = line.split()
result = [float(num) for num in numbers]
result = sum(result)
print(result)