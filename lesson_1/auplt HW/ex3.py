# Lecture 1 Exercise 3

# На стандартном потоке ввода задаётся последовательность чисел.
# На стандартный поток вывода выведите модули целых частей этих чисел.

import math

line = input()
print(", ".join(str(abs(math.trunc(float(ln)))) for ln in line.split()))
