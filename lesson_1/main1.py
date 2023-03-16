enter_numbers = list(input("Enter a list of numbers separated by spaces: ").split())
numbers = map(float, enter_numbers)
print("Outputting the sum of the numbers you entered: ", int(sum(numbers)))