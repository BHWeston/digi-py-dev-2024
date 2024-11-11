# Introduction to how classes work within Python:

# Think of classes as a way of creating a template within our work:
class exampleClass:
    x = 20

# Once we create a class, we can use that class name to create "objects" within our work:
objectName = exampleClass()
# All objects that we create will have access to any variables/methods that we create within the class e.g. in this case the variable X:
print(objectName.x)