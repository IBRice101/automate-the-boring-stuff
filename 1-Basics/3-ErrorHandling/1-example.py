def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("error: divide by zero")

print(div42by(2))
print(div42by(12))
print(div42by(0)) # throws a divide by zero error
print(div42by(1))