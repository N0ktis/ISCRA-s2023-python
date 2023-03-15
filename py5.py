original_string = input()
num = int(input())
modified_string = ''
character_by_character_string = list(original_string)
for i in character_by_character_string:

    modified_string += chr(((ord(i) - 97 + num) % 26) + 97)

print(modified_string)
