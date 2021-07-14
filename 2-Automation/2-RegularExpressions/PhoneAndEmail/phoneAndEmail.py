# NOTE: can be easier by removing need for clipboard and outputting to txt file

import re # regex
import pyperclip # clipboard interaction

# phone number regex
phoneRegEx = re.compile(r'''

# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext|ext.|x 12345

(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)                          # separator (space or dash)
\d\d\d                          # first 3 digits
-                               # separator (dash only)
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s)|x)               # extension (word, optional)
(\d{2,5}))?                     # extension (number, optional)
)

''', re.VERBOSE)

# email regex
emailRegEx = re.compile(r'''

# some.+_thing@some.+_thing.(com|edu|org|net)

(
[a-zA-Z0-9.+_]+         # name
@                       # @ symbol
[a-zA-Z0-9.+_]+         # domain
)

''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract email/phone no.s
extractedPhone = phoneRegEx.findall(text)
extractedEmail = emailRegEx.findall(text)

allPhoneNumbers = []
for phoneNum in extractedPhone:
    allPhoneNumbers.append(phoneNum[0])

# copy extracted data to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
