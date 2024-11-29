# This program will look to introduce some of the more technical topics within OOP:

# Creating our classes:
# This will create a class called Cat, this will be our "blueprint":
class Cat:
    # Create a method that we can use to make the cat say something:
    def meow(self):
        print("Meow")

    # Create a new method that will take a number input and times this by 4 (1 human year is 4 cat years):
    def calcCatYears(self, iEnteredAge):
        # Return the value the users puts in and times this by 4:
        print("The number of cat years for the cat is: ")
        return iEnteredAge * 4
    
class Dog:
    def calcDogHumanYears(self,iEnteredDogAge):
        print("The number of human years for the dog is:")
        return iEnteredDogAge // 7
    
# Using our classes:
dog1 = Dog()
dog1.calcDogHumanYears(14) # This will return 2.0
# To use our classes, we need to "initialise" our template, in other words, provide this with a location that we can use:
cat1 = Cat()
cat1.meow()
# Same as within procedural, we can look to run methods and pass paramaters within these:
iCatAge = int(input("Enter in the age of your cat: "))
print(cat1.calcCatYears(iCatAge))

# Task: Create a new class that will store the details of a dog, this will look to calculate dog years to human years.