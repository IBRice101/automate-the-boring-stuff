'''

Program that takes an address from either args or clipboard and opens the 
address in google maps

'''

import webbrowser
import sys
import pyperclip

sys.argv # ['mapit.py', '123', 'Example', 'Street']

# check if args were passed
if len(sys.argv) > 1:
    # make args one string
    address = ' '.join(sys.argv[1:])
else:
    # take args from clipboard
    address = pyperclip.paste()

print('Opening ' + address + ' in Google Maps')
webbrowser.open('https://www.google.com/maps/place/' + address)
