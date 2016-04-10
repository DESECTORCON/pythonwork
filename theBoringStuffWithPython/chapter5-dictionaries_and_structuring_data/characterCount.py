message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
message = input('write a word: ')
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)