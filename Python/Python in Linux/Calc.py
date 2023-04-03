#!/bin/python3

def get_number(prompt):
	while 1==1:
		try:
			number = int(input(prompt))
			return number
		except ValueError:
			print("Invalid input: please enter a numerical value.")

x = get_number("Enter first value: ")
z = input("What function do you want to do(+,-,*,/): ")
y = get_number("Enter second value: ")

if z == "+":
	print("\n")
	print("The result of the equation is" , x + y)
elif z == "-": 
	print("\n")
	print("The result of the equation is" , x - y)
elif z == "*": 
	print("\n")
	print("The result of the equation is" , x * y)
elif z == "/": 
	print("\n")
	print("The result of the equation is" , x / y)
else:
	print("\n")
	print("Unidentified function")
