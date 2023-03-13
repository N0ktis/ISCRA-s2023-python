from math import floor
string = input()
new_string = ''
nums = string.split()
for numbers in nums:
    abs_num = floor(abs(float(numbers)))
    new_string += str(abs_num) + ' '
print(new_string)
