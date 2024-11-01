# Insertion sort is an alternative way to organising an array, this is done by having a "sorted" and "unsorted" list:

# Create a function which will be used to return our sorting
def insertionSort(array):
    # Create a FOR loop which will go through each item within our array:
    for index in range(1, len(array)):
        # Create a variable which will store our current value in the array
        iCurrentValue = array[index]

        # Create a variable which will store our current index location:
        iCurrentPosition = index

        print(f"The current value is {iCurrentValue}, the current position is {iCurrentPosition}")

        # During the position being greater than 0, and that the current position in our list is greater than the position before:
        while iCurrentPosition > 0 and array[iCurrentPosition-1] > iCurrentValue:
            # Swap the values within the array:
            array[iCurrentPosition] = array[iCurrentPosition-1]
            iCurrentPosition = iCurrentPosition-1
            # print(array)
        array[iCurrentPosition] = iCurrentValue
    return array
#### MAIN ####

# An array of unsorted values:
lUserArray = [10,5,2,11,5,4,5,45,68,55,2,34,45,78]

# Our returned array will go into a variable called "sortedArray":
lSortedArray = insertionSort(lUserArray)

print(lSortedArray)