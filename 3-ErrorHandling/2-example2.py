print('how many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('thats a lotta cats')
    else:
        if numCats < 0:
            print('you can\'t have negative cats!')
        else:
            print('that\'s not very many cats')
except ValueError:
    print('You didn\'t enter a number')