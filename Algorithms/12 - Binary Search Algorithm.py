# Binary Search Algorithm = This requires a sorted list in order to be processed

# FUNCTIONS AREA #
def binarySearch(toFind, items):
    # Get the first item in our list:
    iFirstIndex = 0

    # Get the last item in our list:
    iLastIndex = len(items) - 1

    # While loop to go through each item in our list, so long as the last index is bigger for equal to our first index:
    while(iFirstIndex<=iLastIndex):
        # From this, as this algorithm works in halfs, we want to find the middle number, we do this by doing a floor division:
        iMidIndex = (iFirstIndex + iLastIndex) // 2
        # // is a floor division: This rounds down
        print(f"This is the middle index: {iMidIndex}")

        # If statement to check if the number the user entered is the same as the middle index number:
        if items[iMidIndex] == toFind:
            print("The number is within the list, YAY")
            return 0
        # If the number in the middle is smaller than the number that I am searching for, add one to the first index and loop again:
        elif items[iMidIndex] < toFind:
            iFirstIndex = iMidIndex + 1
        # If the number in the middle is larger the move the last index below the middle index
        else:
            iLastIndex = iMidIndex - 1

iNumberToFind = int(input("Enter in a number that you would like to find within the list: "))
# Creating a sorted list:
# INDEXES      [0,1,2,3,4,5,  6, 7,8, 9, 10,11,12,13,14,15,16,17, 18, 19, 20]
# Running len(items) will give us 21
aSortedArray = [1,3,4,8,9,12,16,18,19,22,26,32,34,36,44,56,78,102,165,201,222]

# Function call that we will use for our binary search algorithm:
binarySearch(iNumberToFind, aSortedArray)