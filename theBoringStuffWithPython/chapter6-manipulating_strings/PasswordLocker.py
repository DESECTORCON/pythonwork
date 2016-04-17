#! /usr/bin/env python3.4
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'tyuri847yuek674YHE734uyeh',
             'blog': 'gdhju5yre647YEH4yrhe',
             'luggage': '123',
             'YL':'1234567890'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
#실패작
'''이유:
'if len(sys.argv) < 2:' 부분에서 sys.argv부분이 잘못되었기 때문'''
# TODO:아빠께 도음받기!
# TODO: updateToGit