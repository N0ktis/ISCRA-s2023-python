#Номер5
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet)
offset = int(input("Encryption step: "))
messages = input("Message: ").upper()
encrypted_message = ''
for message in messages:
    position = alphabet.find(message)
    new_position = position + offset
    if message in alphabet:
        encrypted_message += alphabet[new_position]
    else:
        encrypted_message += message
print(encrypted_message)