#! python3
# PasswordLocker.py - An insecure password locker program.
import sys
import pyperclip

PASSWORDS = {'email': '123!@#45$546%^67&(34564',
             'facebook': 'wervbmn345@@%%$$^^%$454',
             'github': 'qwe6789234jfgfh#9%$#675'}


if len(sys.argv) < 2:
    print('Usage: py PasswordLocker.py[account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + ' copied to clipboard.')
else:
    print('There is no account named' + account)
