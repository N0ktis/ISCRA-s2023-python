# Task №3
import math

if __name__ == '__main__':
    input_list = input().split()
    fabs_int_elements = list()
    for i in input_list:
        fabs_elem = math.fabs(float(i))
        fabs_int_elements.append(int(fabs_elem))
    print(fabs_int_elements)

