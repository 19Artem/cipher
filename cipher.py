message = input("enter your message: ")
key = input("enter your key:")

for char in message:
    new_char = ord(char) + int(key)
    print(char, ord(char), new_char)
      

print(message, key)
