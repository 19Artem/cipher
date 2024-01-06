message = input("enter your message: ")
key = input("enter your key:")
letters = list()
for char in message:
    new_char = ord(char) + int(key)
    print(char, ord(char), new_char, chr(new_char))
    letters.append(chr (new_char))

phrase = "". join(letters)
print(message, key,phrase)
