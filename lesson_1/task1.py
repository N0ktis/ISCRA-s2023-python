# Task №1

def sum(nums):
    sum = 0
    for i in nums:
        sum = sum + i
    return sum

if __name__ == '__main__':
    numbers = []
    n = input()
    for i in range(int(n)):
        x = int(input())
        numbers.append(x)
    print(sum(numbers))
