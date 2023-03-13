#problem_3
nums = input()
abs_nums = [int(abs(num)) for num in [float(num) for num in nums.split()]]
for num in abs_nums:
    print(num, end = " ")