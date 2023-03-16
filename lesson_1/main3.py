enter_numbers = list(input("Enter numbers: ").split())
numbers = map(float, enter_numbers)
a = list(map(abs, numbers))
b = list(map(int, a))
print(*b, sep=' ')


