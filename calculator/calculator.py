#comment out the line below so the code can run
calculator/calculator.py

#here is a really simple example python calculator to show how functions, calculations, libraries, etc are used in python as a basic python script for reference and for learning.

#===================================================================== import the math library to enable the square root function =================================================================

import math

#=================================================================================== display the options for calculations =========================================================================

#you can use \n in strings as used below to create 1 line gaps when its outputted which helps to make a more organised output for the user to read especially for longer strings like below.
#in this calculator example i have used a selection of numbers to help the user to use the necessary calculations while avoiding any issues with spelling mistakes or case sensitivity from inputs.

print(" 1 = add \n 2 = subtract \n 3 = multiply \n 4 = divide \n 5 = square root")

#=============================================================================== create functions for calculations and outputs ====================================================================

#by using functions the code remains organised and you can chain together different functions to do more complicated multiple step calculations if you wanted to.
#line 22 and 23 are used to cast the two variables num1 and num2 from strings to integers so they can be used in calculations.

def addition():
    num1 = input("enter the first number of the calculation     ")
    num2 = input("enter the second number of the calculation        ")
    num1 = float(num1)
    num2 = float(num2)
    answer = (num1 + num2)
    print(answer)

#from here i just copy and pasted and then changed a few things for the rest of the calculations other than square root in order to save time.

def subtraction():
    num1 = input("enter the first number of the calculation     ")
    num2 = input("enter the second number of the calculation        ")
    num1 = float(num1)
    num2 = float(num2)
    answer = (num1 - num2)
    print(answer)

def multiplication():
    num1 = input("enter the first number of the calculation     ")
    num2 = input("enter the second number of the calculation        ")
    num1 = float(num1)
    num2 = float(num2)
    answer = (num1 * num2)
    print(answer)

def division():
    num1 = input("enter the first number of the calculation     ")
    num2 = input("enter the number to divide by     ")
    num1 = float(num1)
    num2 = float(num2)
    answer = (num1 / num2)
    print(answer)

def square_root():
    num1 = input("enter the number to square root       ")
    num1 = float(num1)
    answer = math.sqrt(num1)
    print(answer)


#=============================================================== take input for calculation to use and use functions to complete it ===============================================================

choice = input("enter the number for the calculation to use     ")
choice_int = int(choice)

if choice_int == 1:
    addition()

if choice_int == 2:
    subtraction()

if choice_int == 3:
    multiplication()

if choice_int == 4:
    division()

if choice_int == 5:
    square_root()

