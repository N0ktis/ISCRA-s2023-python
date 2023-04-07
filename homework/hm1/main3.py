#problem4
nums = input()
square_nums = [num**2 for num in [float(iter) for iter in nums.split()]]
sum = 0
for num in square_nums:
    sum+=num
print(sum)