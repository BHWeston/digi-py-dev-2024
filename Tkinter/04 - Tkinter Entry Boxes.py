## Library Imports ##
import tkinter as tk

## Functions ##
def submitText():
    currentValue = userInput.get()
    outputText = tk.Label(text=f"The value your type in was {currentValue}")
    outputText.grid(column=0, row=2)
## Main ##
window = tk.Tk()
window.geometry('500x100')

# Adding in an entry box:
userInput = tk.Entry(text=0)
userInput.grid(column=0, row=0)

submitButton = tk.Button(text="Submit above", command=submitText)
submitButton.grid(column=0, row=1)
window.mainloop()