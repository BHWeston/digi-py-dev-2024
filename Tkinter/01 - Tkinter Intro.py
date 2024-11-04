#### LIBRARY IMPORTS ####

# This is a library which will allow us to work with a front end system, rather than using command line
import tkinter as tk

### MAIN ###

# This initialises a window that will be used within our code:
window = tk.Tk()

# The width and the height of the window:
window.geometry('800x600')

# print("Hello label")

# Create a label that we are going to use:
introLabel = tk.Label(text="Welcome to my program")

# Change the background colour of the label:
introLabel["bg"] = "red"

# This will change the foreground colour of the label:
introLabel["fg"] = "blue"
# This will place the label onto the screen with the below co-ordinates
introLabel.place(x=40, y=30)

# As an alternative way of being able to display data onto the screen, we can use a .grid() command, which will allow for columns and rows to be used instead of co-ordinate positioning:
label2 = tk.Label(text="This label uses a grid")
label2.grid(column=1, row=1)

label3= tk.Label(text="This label uses grid")
label3.grid(column=0, row=0)

# THIS IS IMPORTANT, this keeps the application running:
window.mainloop()