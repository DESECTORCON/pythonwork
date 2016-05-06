#! usr/bin/env python3.4
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip ,re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                    #area code
    (\s|-|\.)?                            #separator
    (\d{3})                               #first 3 digits
    (\s|-|\.)?                            #separator
    (\d{4})                               #last 4 digits
    (\s*(ext|x|ext.)\s(\d{2,5}))?         #extension
    )''', re.VERBOSE)

# TODO: Creat email regex.

# TODO: Find matchs in clipboard text.

# TODO: Copy results to the clipboard.