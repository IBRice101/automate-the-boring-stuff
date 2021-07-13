import re # regex module

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 during the week"

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")# \d is a digit in regex
mo = phoneNumRegex.search(message)
print("Found Number: " + mo.group())
