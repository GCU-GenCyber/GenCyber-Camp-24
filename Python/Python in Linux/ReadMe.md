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

Programming languages allow us to store information in what is called variables. There are many different types of variables and in some languages, we would need to declare what kind of variable we are using, but not in Python. In Python, the variable type will be determined by the content. 

Type the following into the file

    x = "Hello World!"
    
    print(x)

We can see we got the same result as before, but the code was different. 

Loops allow us to do a task over and over again as many times as we want. There are two different kinds of loops in Python, the 'for' loop and the 'while' loop. 
The 'for' loop is used to iterate over a sequence or other iterable objects like a range. 

    for variable in iterable:
        # code

The variable takes the value of each item in the iterable on each iteration of the loop.
