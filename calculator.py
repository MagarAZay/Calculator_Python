
while True:
    try:
         a = int(input('Enter no.1: '))
         b = int (input('Enter no.2: '))
         break
    except ValueError:
            print("Invalid input! Please enter a number.")



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot be divided by 0"
    else:
        return a / b

def exponent(a, b):
    return a ** b

print('Addition:', add(a, b))
print('Subtraction:', subtract(a, b))
print('Multiplication:', multiply(a, b))
print('Division:', divide(a, b))
print('Power:', exponent(a, b))
