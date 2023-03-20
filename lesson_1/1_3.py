from math import fabs
from math import floor
line = input()
numbers = line.split()
result = [float(num) for num in numbers]
absresult = [fabs(res) for res in result]
fabsresult = [floor(absres) for absres in absresult]
print(fabsresult)