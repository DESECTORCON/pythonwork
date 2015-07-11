message = input("매새지를 입력해 주십시오.: ")
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + 13
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("아우푸트 메세지:  ", output)
