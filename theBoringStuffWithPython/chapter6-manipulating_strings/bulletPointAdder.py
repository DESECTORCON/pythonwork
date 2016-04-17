#! /usr/bin/env python3.4
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.-OK!
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexexs for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
print(text)
# TODO: updateToGit