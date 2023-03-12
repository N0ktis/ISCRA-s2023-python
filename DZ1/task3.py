numbers = input().split()
list = [int(abs(float(number))) for number in numbers]
print(list)
