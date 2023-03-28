# Task №4

def encrypting(message, key):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    for i in message:
        index = alfabeth.find(i)
        new_index = index + key
        if i in alfabeth:
            encrypted_message += alfabeth[new_index]
        else:
            encrypted_message += i
    return encrypted_message



if __name__ == '__main__':
    message = input('Input the string: ')
    key = int(input('Input the key: '))
    print(encrypting(message,key))

#puhtuhavtpj

