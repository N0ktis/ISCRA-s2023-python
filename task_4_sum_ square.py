# На стандартном потоке ввода задаётся последовательность чисел.
# Выведите сумму квадратов этих чисел.

nums = input()
nums = nums.split()

result = 0

for num in nums:
    num = float(num)
    num **= 2
    result += num

print(result)