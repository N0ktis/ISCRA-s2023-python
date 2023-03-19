# Task №4

def square_num(num_str):
    num = float(num_str)
    return num*num

def square_list(list_):
    new_list = list()
    for i in list_:
        new_list.append(square_num(i))
    return new_list

def sum(list):
    sum = 0
    s_list = square_list(list)
    for i in s_list:
        sum = sum + i
    return sum

if __name__ == '__main__':
    input_list = input().split()
    print(sum(input_list))
