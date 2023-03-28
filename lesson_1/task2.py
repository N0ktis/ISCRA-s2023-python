# Task №2

def str_change(str, old_s, new_s):
    new_str_list = ''
    for i in str:
        if i == old_s:
            i = new_s
            new_str_list = new_str_list + i
        else:
            new_str_list += i
    return new_str_list

if __name__ == '__main__':
    str = input('The string:')
    old_s = input('Enter the symbol that you want to change:')
    new_s = input(f'{old_s} -> ')
    list_string = str
    print(str_change(list_string, old_s, new_s))
