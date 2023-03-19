# Task №2

def str_change(str):
    new_str_list = ''
    for i in str:
        if i == "A":
            i = '4'
            new_str_list = new_str_list + i
        elif i == "I":
            i = '1'
            new_str_list = new_str_list + i
        elif i == "E":
            i = '3'
            new_str_list = new_str_list + i
        else:
            new_str_list = new_str_list + i
    return new_str_list

if __name__ == '__main__':
    str = input()
    list_string = str
    print(str_change(list_string))
