# Name Output:
# Ask the user to enter in their name into the program (using input)
# Output the name back onto the screen (using print)

print("You will be asked to enter in your name")
sName = input("Enter in your name: ")

# This will output onto the screen the relevant details, however having two "print()" commands will put these onto separate lines:
print("The name you entered was: ")
print(sName)

# If we combine the above but separate by a comma, this will do the same:
print("The name you entered was:", sName)

# Alternative, an f string can be used to combine together, without then need for lots of commas. Variables however need to be inputted into curly braces:
print(f"The name you entered was: {sName}")