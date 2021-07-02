# purposefully wrong

# standard while loop, have to enter 'your name' string literal
name = ''
while name == 'your name':
    print('please type your name')
    name = input()
print('thank you')

# while true loop with break, have to enter 'your name' string literal
while True:
    print('please type your name')
    name = input()
    if name == 'your name':
        break
print('thank you')

# standard while loop with continue, skips 3
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam)) 