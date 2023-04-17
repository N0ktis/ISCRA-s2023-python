def input_data():
    print('Enter main text:')
    text = input()
    print(
        'Enter substitution rules (e. g. A->B, C->D, ...), enter "end" to stop:'
    )
    data = input()
    substitution_rules = {}
    while data != 'end':
        pair = data.split('->')
        substitution_rules[pair[0]] = pair[1]
        data = input()
    return text, substitution_rules


def print_data(text, substitution_rules):
    print('Input data:')
    print(text)
    for i in substitution_rules.keys():
        print(i, substitution_rules[i])


def process_data(text, substitution_rules):
    for i in substitution_rules:
        text = text.replace(i, substitution_rules[i])
    return text


if __name__ == "__main__":
    # text, substitution_rules = input_data()
    text = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
    substitution_rules = {'A': '4', 'I': '1', 'E': '3'}
    text = process_data(text, substitution_rules)
    print(text)