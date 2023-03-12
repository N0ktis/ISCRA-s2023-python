line = ''
shift = 0
new_list = ''

line = input()  # Ввод строки из консоли
shift = input()  # Ввод сдвига из консоли

for character in line:
    code = ord(character)
    new_code = code + int(shift)

    if (code == 1025):  # Ё -> Е
        new_code = 1045 + int(shift)

    if (code == 1105):  # ё -> е
        new_code = 1077 + int(shift)

    if (code == 32):  # ' '
        new_list += (chr(code))

    elif ((new_code >= 1072) & (new_code <= 1103)):
        new_list += (chr(new_code))

    elif (new_code >= 1072):
        new_list += (chr(new_code - 32))

    elif ((new_code >= 1040) & (new_code <= 1071)):
        new_list += (chr(new_code))

    elif (new_code >= 1040):
        new_list += (chr(new_code - 32))

    elif ((new_code >= 97) & (new_code <= 122)):

        new_list += (chr(new_code))

    elif (new_code >= 97):
        new_list += (chr(new_code - 26))

    elif ((new_code >= 65) & (new_code <= 90)):
        new_list += (chr(new_code))

    elif (new_code >= 65):
        new_list += (chr(new_code - 26))

    else:
        print("Что-то поломалось", new_code)

print(new_list)
