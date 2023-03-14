def cesar(line, shift):
    newline = ""
    for i in line:
        newline = newline + chr(((ord(i) - 97 + shift) % 26) + 97)
    return(newline)