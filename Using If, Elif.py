while True:
  try:
      a = int(input('Enter no.1: '))
      b = int (input('Enter no.2: '))
      print('1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n')
      c = int(input('Choose (1-4): '))
      break
  except ValueError:
     print("Invalid! Type a number")
def add(a,b):
     return a+b
def sub(a,b):
     return a-b
def mult(a,b):
     return a*b
def div(a,b):
     if b==0:
         return('Cannot be divide by 0')
     elif a==0:
        return('0 cannot be divided')
     return a/b

if c==1:
 print("Addition: " ,add(a,b))
elif c==2:
 print("Subtraction: " ,sub(a,b))
elif c==3:
 print("Multiplication: ", mult(a,b))
elif c==4:
 print("Division: ", div(a,b))
else:
 print('Please choose between 1-4')


