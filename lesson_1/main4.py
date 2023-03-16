enter_numbers = list(input("Enter numbers: ").split())
numbers = map(float, enter_numbers)
sum_squares = 0
for number in numbers:
    square = number ** 2
    sum_squares += square
print(sum_squares)