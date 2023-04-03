# Python Basics

Python is a popular languarge for scripting in cybersecurity, but it is not only used in this field. Python is a great initial language for anyone interested in programming. 

To start, we are going to need to create a file that will allow you to execute python in the Linux terminal. Go ahead and create a file with the file extention of '.py'. Then, change the permissions of this file to make it executable. 

Here's some commands that will help.

    touch file.py
    chmod +x file.py
    
Now open the file with the editor of your choosing, for this lesson, I will be using gedit.

For Linux, to use the python functions, you will need to add the following to the top of the file.

    #!/bin/python3
    
Now we can begin writing code. 

Type the following into the file.
    
    print("Hello World!")

Save the file and go back to the terminal. In the folder where the python file sits, execute it. You can do so by doing the following. 
    
    ./file.py
    
If everything was done correctly, you should see the terminal printed "Hello World!"

---

### Variables 

Programming languages allow us to store information in what is called variables. There are many different types of variables and in some languages, we would need to declare what kind of variable we are using, but not in Python. In Python, the variable type will be determined by the content. 

Type the following into the file

    x = "Hello World!"
    
    print(x)

We can see we got the same result as before, but the code was different. 

Type the following code

    x = 10
    y = 20
    
    x + y = z
    
    print(z)
    
When running this file, it prints out '30'. The code declares the two variables, 'x' and 'y', then adds them together and sets it to 'z'.

#### Boolean

Boolean values in Python are True and False, representing the truth values of logical expressions. They can be used in conditional statements, loops, and logical operators such as and, or, and not. Python also has a concept of "truthiness" that allows non-Boolean values to be evaluated as Booleans. Any value can be evaluated as a Boolean value, and if it's considered "truthy", it's treated as True; otherwise, it's treated as False. This concept of "truthiness" can be helpful when working with values that aren't explicitly Boolean.

    x = 5
    y = 10
    z = x < y

    print(z)

The 'z' variable is boolean.

---

### User inputs

Python can take the input of the user to store in variables. This can be done by using 'input()'. Inside of the '()' you can put a message asking what you want the user to put in the variable. 

Type in the following code

    name = input("What is your name: ")
    print(name)

After executing this, you can see the terminal asks your name and waits for an input. You are now able to type in your name and can see the code relays back your name. 

---

### Loops

Loops allow us to do a task over and over again as many times as we want. There are two different kinds of loops in Python, the 'for' loop and the 'while' loop. 
The 'for' loop is used to iterate over a sequence or other iterable objects like a range. 

    for variable in iterable:
        # code

The variable takes the value of each item in the iterable on each iteration of the loop.

Type the following code:

    for i in range(10):
        print("Hello World!")

After executing the file, we can see that ten "Hello World!"s were printed.

The 'while' loop allows us to loop through a piece of code while a statement is true. 

    while condition:
        # code

The condition is a Boolean expression that is evaluated at the beginning of each iteration of the loop. The loop continues to execute as long as the condition is true.

Type the following code

    a = 0
    while a < 10:
        print("Hello World!")
        a += 1

To use a condition statement including a variable, you will need to declare it first. This is needed for the loop to understand if the condition is 'True' or 'False'. Once it is determined, if the condition is 'True', it will start the loop. At the end of the code, you can see that there is a line that reads 'a += 1'. This is the python increment code. This will allow us to incriment the variable of 'a' each time it loops through. Without this, this loop would become infinite. If you run this code, you can see that it will print "Hello World!" ten times. 

---

### Functions

Functions in Python are blocks of code that can be called repeatedly, with different inputs, to perform a specific task. Functions are defined using the def keyword, followed by the function name, any necessary arguments, and a colon. The body of the function is indented and contains the code to be executed when the function is called.


Functions can take arguments, which are values passed to the function to be used in the code block. Arguments can be required or optional, and they can have default values.


Functions can also return values, which are the results of the computations performed within the function. The return keyword is used to specify the value to be returned from the function.


Functions can be used to make code more modular, organized, and reusable. They can also help to improve code readability and reduce the potential for errors.

Here is an example

    def sayhi:
        print("Hello World")
    
    sayhi()

---

### If statements


if statements in Python are used to test whether a condition is true or false, and to execute different blocks of code based on the result of the test. The basic syntax of an if statement is to use the keyword if, followed by the condition to be tested, and then a colon. The code to be executed if the condition is true is indented beneath the if statement.


In addition to the basic if statement, there are several related statement types in Python, including else and elif statements. An else statement is used to specify code to be executed if the condition in the if statement is false. An elif statement (short for "else if") is used to test additional conditions if the initial if statement is false.


if statements can be nested inside one another to create more complex tests and conditions. However, it's important to ensure that the indentation of each block of code is correct in order for the code to run properly.


if statements are a fundamental part of programming in Python, and they are used extensively in many types of programs, from simple scripts to complex applications.

Here is an example

    x = 5
    y = 7

    if x < y:
	    print("x is less than y")
    else:
	    print("x is greater than y")
---

### Try and Except

The try and except statements are used in Python to handle errors and exceptions that may occur during program execution.
The try block is used to enclose the code that may potentially raise an exception. If an exception occurs, the program execution is transferred to the except block.
The except block contains the code that is executed when an exception is raised in the try block.
By using try and except blocks, you can prevent your program from crashing due to errors and handle them gracefully.
It is considered good practice to be specific in the types of exceptions you catch, so that you can handle them in an appropriate manner.

	try:
		age = int(input("Enter your age: "))
		print("Your age is", age)
	except:
		print("Invalid input")

---

### Challenge 

We can now try to put all of these components into one script and see what we can make. 

We are going to make a calculator. 
I have found it best to start simple, then continue to add to the program until I have created what I wanted. This makes it easier to find issues as I am programming. 

    x = 5
    y = 2

    print(x + y)

There we go, simple calculator. Now we can add the user input.

    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))

    print(x + y)
    
Now the user can add numbers together. Let's make it so the user can choose what they want to do with the numbers.

    x = int(input("Enter first value: "))
    z = input("What function do you want to do: ")
    y = int(input("Enter second value: "))

    if z == "+":
	    print(x + y)
    elif z == "-": 
    	print(x - y)
    elif z == "*": 
    	print(x * y)
    elif z == "/": 
    	print(x / y)
    else: 
    	print("Unitentified function")
        
Good, but a user can cause some errors if they put the wrong inputs in. 

	def get_number(prompt):
		while 1=1:
			try:
				number = int(input(prompt))
				return number
			except ValueError:
				print("Invalid input: please enter a numerical value.")

	x = get_number("Enter first value: ")
	z = input("What function do you want to do: ")
	y = get_number("Enter second value: ")

	if z == "+":
		print(x + y)
	elif z == "-": 
		print(x - y)
	elif z == "*": 
		print(x * y)
	elif z == "/": 
		print(x / y)
	else: 
		print("Unidentified function")

Now we are going to add some final touches to it, these will make it easier for the user to read the results and understand how to use the program a bit better. 

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
		
There you go, you have created a simple calculator in Python. 
