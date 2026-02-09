#Python bootcamp week first assignment

#QUESTION NO.1 :
#Create a variable name and store your name in it. Print the value

#solution:
name = "Ibad-ur-rahman zafar"
print("name :" , name)


#QUESTION NO.2 :
#Create two variables age and height .Print both values.

#solution:
age = 21
print("AGE : " , age)

height = 6
print("height : " , height)

#QUESTION NO.3 :
#Sore a number in a variable and print its data type using type().

#solution:
marks = 1034
print(marks , type(marks))

#QUESTION NO.4 :
#create a variable is_student and store True in it and print the value

#solution:
is_student = True
print(is_student)

#QUESTION NO.5 :
#Take one number from user and store it in a variable . print the value

#solution:
num = input("Enter a number : ")
print("Number : ",num)

#QUESTION NO.6 :
#Take two numbers from user and print its sum.

#solution:
num1 = 40
num2 = 50
print("sum  is equal to : ", num1+num2)

#QUESTION NO.7 :
#Take two numbers and check which one is greater using if.

#solution:
num1 = 20
num2 = 10
if num1>num2:
    print("num1 is greater than num2")

#QUESTION NO.8:
#Take a number and check whether it is even or odd:

#solution:
number = 25
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")

#QUESTION NO.9:
#Take marks as input and print:
#=>Pass if marks are 50 or above
#=>otherwise fail

#solution:
marks = int(input("please enter your marks : "))
if marks>=50:
    print("Pass")
else:
    print("Fail")

#QUESTION NO.10:
#Take a number and check
#less than 10
#equal to 10
#greater than 10

#solution:
num3 = int(input("Enter a number : "))
if num3 < 10:
    print("The number is less than 10 ")
elif num3 == 10:
    print("The number is equal to 10 ") 
else:
    print("The number is greater than 10 ")   
