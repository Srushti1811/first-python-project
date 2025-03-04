#conditional Operators
# < , > , >= , <= , == , !=

a=int(input("Enter the value a : "))

# #if-else statement

if(a>=50):
    print("Your value is greater than 50")
else:
    print("Your value is less than 50 !!!")


#if-else-elif statement

num=int(input("Enter the value of num : "))

if(num>0):
    print("Value of num is positive : ")
elif(num==0):
    print("Value of num is Zero!!!")
else:
    print("Value of num is Negative..")

#Nested if statement

b=int(input("Enter the number to check whther it is Even number or Odd number : "))

if(b==0):
    print("Enter a postive number to check if its Even or Odd")
elif(b%2!=0):
    print("This is a Odd number")
elif(b%2==0):
    print("This is a Even number")
else:
    print("Enter a valid number")