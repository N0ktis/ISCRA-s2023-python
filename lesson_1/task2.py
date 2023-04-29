current_str = input()
while(True):
    replace_arr = input().split("->")
    current_str = current_str.replace(replace_arr[0], replace_arr[1])
    print(current_str)
