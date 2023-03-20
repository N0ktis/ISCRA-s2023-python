print('введите строку с числами')
num_line = input()
nums = list(float(num) for num in num_line.split())
print(sum(nums))
