# На стандартном потоке ввода задаётся последовательность чисел.
# На стандартный поток вывода выведите модули целых частей этих чисел.

nums = input()
nums = nums.split()

numeral = []
number = []

for num in nums:
    num = num.split('.')
    numeral.append(num[0])

for num in numeral:
    number.append(int(num))

absolute = [abs(element) for element in number]

print(absolute)