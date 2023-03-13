original_string = input()
num = int(input())
ascii_code = []
new_ascii_code = []
modified_string = ''
character_by_character_string = list(original_string)
for words in character_by_character_string:
    ascii_code.append(ord(words))

for modified_ascii_code in ascii_code:
    new_ascii_code.append(modified_ascii_code+num)

for new_code in new_ascii_code:
    modified_string += chr(new_code)

print(modified_string)
