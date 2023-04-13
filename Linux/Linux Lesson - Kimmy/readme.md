# Beginners: Lesson 1
## Root and File System

Log into Kali:
```
User: toor
Pass: root
```

It is important to know that in Linux **root** is similar to the Windows' **Administrator**. Those privileges are not given to every user, and we will go over privileges and permissions later. 

Right now, we are just going to learn how to look at Linux's file system. Find Kali’s version of File Explorer and explore the files. Don’t open anything, just look at file names and see how far back you can get into the files. Windows starts at the C drive, but where does Linux start?

Find the Root directory. What is in the root directory? 
(A directory is a folder that contains files)

As stated before, root is a user, like an admin. It’s the user with the most privileges. Just like in Windows, all of the files belonging to the user (Desktop, Documents, etc.) are under that user’s name. Take a minute to explore the file system and see if you can find any differences or similarities between Linux and Windows. 


## Settings

Find the Following Settings and Applications:

Desktop Background
- Change it to one of the pre-installed ones
Mousepad (Application)
- Open
- Write hello world!
- Name it hello and Save it to your Documents folder
- Exit 

## Terminal Usage vs. GUI

Continue to Explore Kali
What happens when you click on the tools? Well, most of them pull up what is called a terminal. Kali is mostly used via a terminal. Windows uses more GUI than Linux. What’s a GUI?
- Graphical User Interface
- all the nice windows that pop up when you click on an application

For example, when you click on the file system application, that’s a GUI. You have visuals to see what you’re doingSince Linux is mostly used via a terminal, how do we go through the file system without a GUI?
- Open up the terminal application on your machines.
- It is important to note, terminals don’t work like google. They are extremely case and spelling sensitive. 
- You need to know commands to be able to use the terminal.

## Commands for File Navigation

- pwd: tells you where you are
	- Remember how the user’s files are under the users name? We can still find those files and see them in the terminal

- ls : to see the files and folders that are in your current location (or file path)
	- All of the things in blue are directories
	- Those are the other folders that we can move to
 
__Remember the mousepad file you made earlier? What folder is the hello in? How do we get there to read it?__
- cd: change directory
	- cd Documents
	- ***LINUX IS CASE SENSITIVE!!*** 
	- Assume everything is lowercase unless you see otherwise, like a file or directory name

Use ls to list the files in your current directory, which should be documents. You should see the hello file you created. But, how do we read what it says?
- cat: will read the file
	- Do "cat hello" in the terminal

Now you know how to navigate through a file system. Here are some more examples of basic linux commands that are extremely helpful. 


mkdir : makes a directory
```
mkdir Files
```
<sub>This command will make a directory named Files in Your Current Location</sub>


rm : removes the file named after the command
```
rm hello 
```
<sub>This command deletes the file we created named hello (if you're in its current location)</sub>


touch : creates a file
```
touch hello 
```
<sub>This command creates a file in your current directory named hello</sub>


--help or -h : pulls up a help page for whatever application you ask
``` 
hydra --help 
```
<sub>This command will pull up a help page for a password bruteforcer called Hydra</sub>


man : pulls up manual/manpages for a tool
```
man hydra
```
<sub>This command will show a manual for a password bruteforcer called Hydra</sub>


cp : copies a file to a different file path
```
cp hello /root/Documents 
```
<sub>This command will move the file named hello to the specified path. The syntax is as follows "cp [FILENAME] [FILEPATH]"</sub>


mv : to move a file
```
mv hello /root/Documents
```
<sub>This command will move the file hello into the specified path. It is similar to cutting and pasting. The syntax is as follows "mv [FILENAME] [FILEPATH]"</sub>


mv: to rename a file
```
mv hello hello1 
```
<sub>This command renames a file. The syntax is as follows "mv [CURRENTFILENAME] [NEWFILENAME]"</sub>


find : to find a file in your computer
```
find / -name hello.txt 
```
<sub>This command will locate a file for you. The syntax is as follows "find [where to start searching from] [options] [what to find]"</sub>


### Extra Linux Rules
- Case Sensitive
 - You have to specify the path of where you want to go like /root/Documents or go into the documents folder to see anything in there
 - If you accidentally run something you aren't supposed to or want to stop, use __Ctrl+C__ end it

# Beginners: Lesson 2
- File Permissions 
	- You can only access a File if you have permission to see it
	- As root, you can see or change anything you want
	- Not that you should, but you have the ability to
	- So how do you see file permissions

Find the hello.txt you created with Mousepad 
- Right click on it
- Click properties
- Click Permissions
You can see the owner, the owner’s group, and others who can see the file. It also specifies the access they have to that file (Read, Read & Write, etc.)

Now check for file permissions in a Terminal
- Open a terminal
- Enter 
```
ls --help
```
The - is a switch (or an option) that gives the command more specifics. There are two options that will help in this case. 
- a : shows all files, even hidden ones (Yes there are hidden folders, Windows has those too.)
- l : long listing format meaning more information
You can combine them both together so instead of using ls -l -a it’s ls -la

This gives you the 
- file permissions
- the owner (creator) of the file
- the group to which that owner belongs to
- the date of creation
				
## Linux File Permissions Tutorial: How to View and Change Permission 
![alt text](https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Linux/Linux%20Lesson%20-%20Kimmy/img/BasicPermissions.png)

The file type will appear as a **-** , **d**, or **i** : file, directory, or link

As seen in the picture, R W X means read, write, and execute.Those are the 3 permissions on Linux. Now, take a look at the hello file that we created. What does it say for the permissions?
	-rw-r--r--
	- **-** means it is a file
The first rw- means the user can read and write or modify it, no execute
			R-- means the group can only read it
			R-- means others can only read it
			The next two words are the owner and group
			
# Beginners: Lesson 3
- Changing file permissions
- The command for that: chmod
- You type chmod [permission] [file_name]
- You can only do this if you have the permission to do so
- Since you are root, it’s allowed
- You have to specify the permissions for each section. For example:
- chmod u=rwx,g=rwx o=rwx hello (if you’re in Documents)
- No spaces, no capitals
- You just changed file permissions to read write and execute for the user, group, and owner of hello
- Go ahead and ls -la again
- Now hello should say -rwxrwxrwx
- Try and use the chmod commands to set the permissions back to normal
- Make the user allowed to read and write 
- Make the members allowed to read
- Makes others allowed to read

### 5 Min Later
- Should be chmod u=rw,g=r,o=r hello
- Instead of letters, the octal format represents privileges with numbers:
- r(ead) has the value of 4
- w(rite) has the value of 2
- (e)x(ecute) has the value of 1
- no permission has the value of 0

- The privileges are summed up and depicted by one number. Therefore, the possibilities are:
- 7 – for read, write, and execute permission
- 6 – for read and write privileges
- 5 – for read and execute privileges
- 4 – for read privileges

As you have to define permission for each category (user, group, owner), the command will include three (3) numbers (each representing the summation of privileges).
- chmod u=rw,g=r,o=r hello command.
- chmod 644 hello
- At some point cd . and cd ..
- Explain what . and .. is

# Intermediate: Lesson 1
- echo and cat 
- nano hello.txt
- sudo apt update
	- Sudo just runs the command with root privileges so this would work without sudo if you were logged in as root as well. Will only work if that user has been given sudo privileges
- df 
	- Shows available disk spaces
	- Can use -m to show in megabytes
- zip and unzip
	- zip and unzip hello
- chmod 
	- You can add individual permissions by using +r, +w, or +x to a file
- hostname
	- Prints host name
	- hostname -i gives you your ip address
- ping google.com or 8.8.8.8
- whoami

# Intermeadiate: Lesson 2
- What does rm -rf / do?
	- Removes with all directories and their contents with force
	- DONT DO IT
- But what is /?
	- / means the root directory
	- Which is everything, it holds all the files and directories
 
Go back to the Documents folder
- Pwd and tell me where you are
- /root/Downloads : / means look at the very tippy top of the directory and follow the path from there
- Don’t get root directory confused with the root user, those are two different things
- 
Open /bin (Binaries)
- See anything familiar?
- It holds the executables of a lot of commands
- It has ls, chmod, and more
- This means that commands are just executables that we are calling to 
- Linux Directory Structure Explained for Beginners (linuxhandbook.com)
 
# Advanced: Tools
### Networking: 
- Ifconfig
- netdiscover
- Nmap
- Wireshark
### OSINT:
- Recon-ng
- Google Dorking
### Cryptography/Hashing:
- CyberChef
- Learn how to hash
- Then hash cat or jtr
### Digital Forensics:
- Autopsy
- FTK Imager
- CSI Linux
- Volatility
