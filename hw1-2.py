string = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
string2 = "WHY THE HELL DO I NEED WHILE TRUE HERE"
def replacement(stcringe):
    while True:
        print(stcringe.replace('A', '4'))
        print(stcringe.replace('I', '1'))
        print(stcringe.replace('E', '3'))
        break

replacement(string)
replacement(string2)

# okay check this
replacements = {'A': '4',
                'I': '1',
                'E': '3'}
for letter in replacements:
    while letter in string:
        string = string[:string.find(letter)] + replacements[letter] + string[string.find(letter) + 1:]
    print(string)
