# This program will look to add in buttons that the user can interact with:

## LIBRARY IMPORTS ##
import tkinter as tk

## FUNCTIONS ##
def helloWorld():
    print("Hello world")

## MAIN ##
window = tk.Tk()
window.geometry('400x400')

# Add a label that says "Welcome to my amazing program", with background colour of blue
welcomeLabel = tk.Label(text="Welcome to my amazing program")
welcomeLabel["bg"] = "blue"
welcomeLabel.grid(column=0,row=0)

# Button that we are going to use within our program, this will display a message on click:
clickButton = tk.Button(text="Please click me", command=helloWorld)
clickButton.grid(column=0, row=1)

# THIS WILL ALWAYS GO AT THE END:
window.mainloop()