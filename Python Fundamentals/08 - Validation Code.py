# Code which will look to validate against a list of poor passwords, and check password validation:

# List of poor passwords
lPoorPassword = ["password", "12345", "asdf", "letmein", "qwerty"]

iNumberInPass = 0
# Check against that list

# Bool that will check if the passwords meets the requirements: (THIS IS CALLED A FLAG)
bFound = False

sUserPassword = input("Enter in your password: ")

# A FOR loop that iterates through the list of items:
for iCounter in range(len(lPoorPassword)):
    if sUserPassword == lPoorPassword[iCounter]:
        print("This password is within a predefined list, this should not be used")
        bFound = True

# Check the size of a password:
if len(sUserPassword) < 8:
    print("The password is too short, please use 8 characters")
    bFound = True

# Format check = Check against types of inputs
for iCounter in range(len(sUserPassword)):
    # Checking if there is a digit in my password (isdigit method):
    if sUserPassword[iCounter].isdigit():
        iNumberInPass = iNumberInPass + 1
        # print("You have a number in your password")
if iNumberInPass == 0:
    print("You should add a number to your password")

if bFound == False:
    print("Your password passes our checks")

# Check isalpha
# Check isupper
# Check islower
# Ext - Can you convert the above sections into suitable functions to breakdown the programme further