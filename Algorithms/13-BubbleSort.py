# Main #
# Create list of numbers that we want to sort:
lValuesToSort = [12,77,55,11,13,145,12,5]

# Get the final index number:
iIndexLength = len(lValuesToSort) - 1

# Create a flag of false to identify if it has been sorted:
bSorted = False

while not bSorted:
    # Go through the list starting from 0:
    bSorted = True
    for iCounter in range(0, iIndexLength):
        if lValuesToSort[iCounter] > lValuesToSort[iCounter+1]:
            bSorted = False
            # A switch variable, is essentially a third place to store our number, so that we can swap them:
            # This stores the first number
            iSwitch = lValuesToSort[iCounter]

            # This swaps the first number with the second number:
            lValuesToSort[iCounter] = lValuesToSort[iCounter+1]

            # This swaps the second number with the first:
            lValuesToSort[iCounter+1] = iSwitch

print(lValuesToSort)