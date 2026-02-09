###############--------- WEEK 1ST MINI PROJECT---------################


# PROJECT TITLE (check positive ore negative number)

#task:
#take one number from user
#use if-slse statement
#print weather the number is positive or negative

#RULES:
#use only variables , operators and if-else 
#no functions and loops

#solution:
num = int(input("Please enter a number : "))
if num<0:
    print("The number is negative ")
elif num>0:
    print("The number is positive")
else:
    print("The number is equal to zero")