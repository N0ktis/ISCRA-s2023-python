enter_text = input("Enter text caps lock: ")
print(enter_text)
prompt = "Enter 'quit' to end the program "
message = ""
while message != 'quit':
    a = input("Enter the letter you want to replace: ")
    b = input(f"Change the letter {a} to ")
    enter_text = enter_text.replace(a, b)
    print(enter_text)
    message = input(prompt)
if message != 'quit':
    print(message)