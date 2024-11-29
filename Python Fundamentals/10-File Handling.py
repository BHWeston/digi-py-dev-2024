# We are going to create a new file that we will be referencing within this session:
# testFile = open("test.txt", "w")

# w = write
# a = append
# r = read
# x = create

# We can add new details onto a file, through the following:
# testFile.write("Hello World")

# YOU MUST ALWAYS RUN THE BELOW COMMAND BEFORE YOU RUN THE SCRIPT:
# testFile.close()

# The above works although is not great practice, the following is better practice:
with open('test.txt','w') as testFile:
    testFile.write("It's a new world")

# Read to a file - This is if we are wanting to output details onto the screen from a .txt file:
with open('test.txt', 'r') as testFile:
    fileContents = testFile.read(50)
    print(fileContents, end='')