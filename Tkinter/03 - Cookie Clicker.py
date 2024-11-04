import tkinter as tk

global iUpgradeValue
iUpgradeValue = 1
iNumbOfClicks = 0
def clickedButton():
    global iNumbOfClicks
    global iUpgradeValue
    iNumbOfClicks += (iUpgradeValue*1)
    clickLabel = tk.Label(text=f"You have clicked {iNumbOfClicks} times")
    clickLabel.grid(column=0, row=2)

# Upgrade button/function
def upgradePoints():
     global iUpgradeValue
     if iNumbOfClicks >= 50:
        iUpgradeValue = iUpgradeValue * 2

screen = tk.Tk()
screen.geometry('400x400')

clickButton = tk.Button(text="Clicker", command=clickedButton)
clickButton.grid(column=0, row=0)

upgradeButton = tk.Button(text="Upgrade for 50", command=upgradePoints)
upgradeButton.grid(column=0, row=1)

screen.mainloop()

# Double Points button when the user reaches 50 points
# Allow for powerups to increment the score
# Have a reset button
# Allow the user to end the game at 1000 points