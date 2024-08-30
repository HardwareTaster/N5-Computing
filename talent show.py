#Anton
#Task 14
name = input('Enter your name')
age = int(input('Enter your age '))
while age<11 or age>18:
    print('Invalid age ')
    age = int(input('Enter your age '))
print('Welcome to the talent show ',name,)
