# Lecture 1 Exercise 4

# На стандартном потоке ввода задаётся последовательность чисел.
# Выведите сумму квадратов этих чисел.

print(sum(float(ln) ** 2 for ln in input().split()))
