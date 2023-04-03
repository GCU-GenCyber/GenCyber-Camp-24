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

    def gotmilk:
        print("Hello World")
    
    gotmilk()

---

### If statements
