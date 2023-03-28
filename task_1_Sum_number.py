# На стандартном потоке ввода задаётся последовательность чисел.
# На стандартный поток вывода напечатайте сумму этих чисел.

nums = input()
nums = nums.split()

result = []

for num in nums:
    result.append(float(num))

print(sum(result))