#addition
def func(a, b):
  return a + b
print (func(1, 2))
    
    
#subtraction
def number(a, b):
  return a - b   
print (number(3, 2))


#multiplication
def multi_two_numb(a, b):
    return a * b
print (multi_two_numb(7, 3))


#division
def div(a, b):
    if b == 0:
        return "Can't divide by zero"
    else:
        return a / b
print (div(25.0, 3))


#addition_all(*args)
def summ(*args):
    x = 1
    for i in args:
        x += i
        print (x)
summ(2, 4, 5, 6)

#subtraction_all(*args)
def sub(*args):
    x = 1
    for i in args:
        x -= i
        print (x)

#multiplication_all(*args)
def mult(*args):
    x = 1
    for i in args:
        x *= i
        print (x)
mult(4, 5, 6)
