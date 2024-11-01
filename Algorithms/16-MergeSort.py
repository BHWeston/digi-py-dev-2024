## FUNCTIONS ##
def mergeSort(array):
    # Get the length of the array:
    iArrayLength = len(array)

    # Check if the length is greater than 1:
    if(iArrayLength>1):
        # print("The array length is greater than 1")
        # Get the middle value of the length:
        iMidLength = iArrayLength // 2

        # Split out array into 2, left and right:
        lLeftArr = array[:iMidLength]
        lRightArr = array[iMidLength:]

        print(f"The left array {lLeftArr}")
        print(f"The right array {lRightArr}")

        # Recurisvely run our function:
        mergeSort(lLeftArr)
        mergeSort(lRightArr)

        # Declare your iterators:
        iLeftIterator = 0
        iRightIterator = 0
        iMainIterator = 0

        # Run the below while the iterator is less then both the left and right arrays:
        while iLeftIterator < len(lLeftArr) and iRightIterator < len(lRightArr):
            if lLeftArr[iLeftIterator] < lRightArr[iRightIterator]:
                array[iMainIterator] = lLeftArr[iLeftIterator]
                iLeftIterator += 1
            else:
                array[iMainIterator] = lRightArr[iRightIterator]
                iRightIterator += 1
            iMainIterator += 1
        # THIS DOES THE MERGE PART FOR OUR ALGORITHM:
        while iLeftIterator < len(lLeftArr):
            array[iMainIterator] = lLeftArr[iLeftIterator]
            iLeftIterator += 1
            iMainIterator += 1

        while iRightIterator < len(lRightArr):
            array[iMainIterator] = lRightArr[iRightIterator]
            iRightIterator += 1
            iMainIterator += 1

    return array
## MAIN ##

lArrayValues = [10,5,1,3,4,56,4,8,7,5,9,12]
print(mergeSort(lArrayValues))