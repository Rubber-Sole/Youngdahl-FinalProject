#!/usr/bin/env python3

# Final Exam - Youngdahl-FinalProject.py
# A calculator that will determine if a value is evenly divisible by either 3, 5, or 3 and 5 together, utilizing modulus operators.
# Dylan Youngdahl CSCI-1103-W03 (WORKS REFERENCED BELOW)
# Date - 9 August, 2022

"""
As a user I want an application that will allow me to know which numbers in a range of values are evenly divisible first by 3, then by 5, and then by both 3 and 5.

    Read string input from the console and convert input to required numeric data-types
    Understand how to use the Python Modulo Operator
    Understand the if / elif / else construct
    Understand how to implement a loop
    Output information back to the user
"""


start_value, ending_value = None, None

while start_value or ending_value == None:
    try:
        start_value = int(input('Please enter starting value: '))
    except ValueError:
        print('Please enter only a whole number! ')
        continue
    try:
        ending_value = int(input('Please enter ending value: '))
    except ValueError:
        print('Please enter only a whole number! ')
        continue
    else:
        break
    
    
def calculator(): # (1) 
    print('\n')
    for num in range(start_value, ending_value + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, '- divisible by both')
            continue
        elif num % 3 == 0:
            print(num, '- divisible by 3')
            continue
        elif num % 5 == 0:
            print(num, '- divisible by 5')
            continue
        else:
            print(num)
        
        
calculator()
    
    
"""
References:
(1) https://www.w3schools.com/python/python_operators.asp
"""
