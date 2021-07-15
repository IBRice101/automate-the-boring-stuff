# create a box that looks like this:

'''

*************
*           *
*           *
*           *
*************

'''

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('the symbol needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('the width and height need to be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

symbol = input("What symbol would you like to use?\n")
width = input("How tall would you like the box?\n")
height = input("How wide would you like the box?\n")

boxPrint(symbol, int(width), int(height))
