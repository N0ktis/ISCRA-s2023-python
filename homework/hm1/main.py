#problem_1
words = input().split()
numbers = [float(word) for word in words]
sum = 0
for i in numbers:
    sum += i
print(sum)