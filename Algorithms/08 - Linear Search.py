# Linear Search = Goes through a list of items to find a result.

# List of items that we want to search within:
lPeopleList = ["Fred", "George", "Ben", "Billy", "Cam", "Terry", "Gerry", "Larry"]

# Ask the user for what name they would like to find within the list:
sNameToFind = input("Enter in the name that you want to find: ")

# Create a "flag" that can be used within the algorithm:
bNameFound = False

# len() gets the length
print(len(lPeopleList))

iNumberOfItems = len(lPeopleList)

# We are going to check through each item within the list, to do this, we are going to use a FOR loop. FOR loops contain the following
# FOR counter in range(endNumber):
for iCounter in range(iNumberOfItems):
    # Check if the name to find is the same as the item in the list:
    if sNameToFind == lPeopleList[iCounter]:
        print("You have found the name")
        bNameFound = True

if bNameFound == False:
    print("You have not found the name")