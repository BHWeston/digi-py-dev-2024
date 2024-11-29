# Introduction to Input and Output
The following markdown guide will look to go through how input and output can work within Python development.

## Input/Output
When looking to display information to a user, you can use the **print()** command:
```python
print("Hello World")
```
> Hello World

Asking for a user to input in commands can be done by using the **input()** command, whatever is put within the parentheses will be prompted to the user:
```python
input("Enter in your firstname:")
```
This is what is outputted onto the user, in this example, a user has typed in "Frank" into the console:
> Enter in your firstname: **Frank**

## Variables
When using an **input()** by itself however, the information does not get stored anywhere, this is where **variables** will need to be used.
```python
sFirstName = input("Enter in your firstname: ")
print(sFirstName)
```
This is the output of the above:
> Enter in your firstname: **Frank**<br/>
> Frank

## Arithmetic
Python can make use of a range of arithmetic operators (+, -, /, *, %, **, //), good practice for doing this is to store information within variables after that are calculated. Some examples of this have been given below.
```python
x = 3 + 4
print(x)
```
Output:
>7

Making use of minus values:
```python
iFirstNum = 1
iSecondNum = 26
iAnswer = iSecondNum - iFirstNum
print(iAnswer)
```
Output:
>25