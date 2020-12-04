###############################################
#                                             #
#       Author UjjwalSharma 19/10/2020        #
#               Version 1.3                   #
#               							  #
###############################################

import string
from tkinter import *
from tkinter import Tk
import os
from time import time
import pyperclip

randPass=""
# For Generating random number
def rand_num(x,y):
   sub=y-x
   z=int(time() - float(str(time()).split('.')[0]))
   random=int((time() - float(str(time()).split('.')[0]))*(10**16))
   random %=sub
   random+=x
   return random

# For Generating time in seconds
def rand_val():
   random=float((time() - float(str(time()).split('.')[0]))*(0.001))
   return random

# For Generating random character
def rand_char(x,y):
   sub=y-x
   z=int(time() - float(str(time()).split('.')[0]))
   random=int((time() - float(str(time()).split('.')[0]))*(10**16))
   random %=sub
   random+=x
   return chr(random)

# For Generating random element
def rand_ele(element):
    a=rand_num(1,11)
    if element==1:
        x=rand_char(33,48)
    elif a==1:
        x=rand_char(65,91)
    elif a==2:
        x=rand_char(97,123)
    elif a==3:
        x=rand_char(33,48)
    elif a==4:
        x=rand_num(1,10)
    elif a==5:
        x=rand_char(33,127)
    elif a==6:
        x=rand_num(1,10)
    elif a==7:
        x=rand_char(58,65)
    elif a==8:
        x=rand_char(65,91)
    elif a==9:
        x=rand_char(91,97)
    elif a==10:
        x=rand_char(97,123)
    return x

# Converts the input list to string
def listToString(arr):
    str = ""
    for element in arr:
        str += element
    return str

# Prints the generated password to the output box
def click():
    password = generatePassword()
    output.delete(0.0, END)
    global randPass
    try:
        randPass = listToString(password)
    except:
        randPass = "There is somethong wrong :("
    output.insert(END, randPass)

# Clears the output box
def clear():
    output.delete(0.0, END)

# Generates the required specifications in the password.
def generatePassword():

    length = rand_num(12,33)
    password = [length]
    for element in range(length):
        import time
        time.sleep(rand_val())
        password.append(str(rand_ele(element)))

    length = len(password)

    # Make first char small letter
    password[0] = rand_char(97,123)
    # time lapse for randomization
    import time
    time.sleep(rand_val())
    # Make last char capital letter
    password[length - 1] = rand_char(65,91)

    return password

# Copies the contents of the varible randPass to the clipboard
def copyToClipboard():
    pyperclip.copy(randPass)

# This is the driver function which creates the window and displays the buttons, and
# prints the output
if __name__ == "__main__":

    win = Tk()
    win.title("Password Generator")

    Label (win, text="Click generate to get a new random password :",
                bg="white",
                fg="black",
                font="ariel 20 bold").grid(row=0, column=0, sticky=N)

    Button(win, text="Generate",
                width=8,
                command=click) .grid(row=3, column=0, sticky=E)

    output = Text(win, width=40, height=1, wrap=WORD, background="white")
    output.grid(row=5, column=0, columnspan=2, sticky=W)

    Button(win, text="CLEAR",
                width=5,
                command=clear) .grid(row=11, column=0, sticky=E)

    Button(win, text="Copy to clipboard",
                width=17,
                command=copyToClipboard).grid(row=10, column=0, sticky=E)

    win.mainloop()
