# Ask the user to enter in a number:

userNumb = int(input("Enter in a number: "))

# This checks if the number is positive (greater than 0)
if userNumb > 0:
    print("This is a positive number")
# This checks if the number is negative (less than 0)
elif userNumb < 0:
    print("This is a negative number")
# If this is neither positive or negative
else:
    print("This is 0")