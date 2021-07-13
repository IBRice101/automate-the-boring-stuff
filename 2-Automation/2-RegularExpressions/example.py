# purposefully verbose code, can be made easier with a single regex

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not a phone number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # no delimiter
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first three digits
    if text[3] != '-':
        return False # no delimiter
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # no last four digits
    return True

number = input()

if isPhoneNumber(number) == True:
    print(str(number) + " is a valid number in the US and Canada")
else:
    print(str(number) + " Is not a valid number in the US and Canada")

