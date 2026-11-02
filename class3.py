# input and output

# name= "harsh"
# age= "20"

# print("hello your name is",name,"and your age is",age)
# print(f"hello your name is {name} and your age is {age}")         #f- formated string
# two ways of using variables inside print statement


#inputs

# age= input("what is you age : ")
# print(f"your age is {age}")

# age= int(input("what is your age : "))    
   #we have to use variable conversion becoz the value that is stored is string to change string to int becoz we can add 10 only in int
# print(f"yoy age after 10 year will be {age +10}")     

#always use type conversion

#opreators

# a = int(input("a = "))
# b = int(input("b = "))

# print(f"sum is {a+b}")

# print(f"division is {a/b}")   #if no is in point then it will come in float

# print(a//b)   #// remove all value after point, known as float division

# print(a**b)    #it mean a^b


# take input of 3 number P, Q, T and calculate the simple intrest

# a = int(input("P = "))
# b = float(input(" Q = "))
# c = int(input("T = "))

# print(f" simple intrest is {(a*b*c)/100}")




#Operator practice sheet   22/09/26
# Q1)  Take input of 2 number and add them.

# a= int(input("A = "))
# b= int(input("B = "))

# print(f"sum is {a+b}")


# Q2)  Take input of 2 number and subtract the second number from the first number.

# a= int(input("A = "))
# b= int(input("B = "))

# print(f"Subtraction is {b-a}")


# Q3)   take input of 2 number and multiply them.

# a= int(input("A = "))
# b= int(input("B = "))

# print(f" multiplication is {a*b}")


# Q4)   Take input o f2 number and divode the first number by the second number.

# a= int(input("A = "))
# b= int(input("B = "))

# print(f"division is {b/a}")



# Q5)  Take input of a price and quantity and calculate the total cost.

# a= float(input("Enter the Price : "))
# b= int(input("Enter the quantity : "))

# print(f"The total cost is {a*b}")


# Q6)  take input o fmarks of 3 subjects and calculate the average marks.

# a= int(input("Enter marks of 1st Subject : "))
# b= int(input("Enter the marks of the 2nd subject : "))
# c= int(input("Enter the marks of 3rd subject : "))

# print(f"the average marks are {(a+b+c)/3}")

# Q8)   take input of minutes and convert them into hours and remaning minute.

# a= int(input("Enter minutes : "))

# print(f"{a} minutes is equal to {a//60} hours and {a%60} minutes")

# Q7)  take  input of a number and find its square. 

# a= int(input("Enter number : "))
# print(f"Square is {a**2}")  

# Q9) Take input of a number and find its remainder when divided bt 5

# a= int(input("Enter number : "))
# print(f"remainder when divided by 5 is {a%5}")

# Q10)   Take input of 2 number and find the first number raised to the 2nd number

a= int(input("Enter the first number : "))
b= int(input("Enter the second number : "))
print(f"first number raised to the power of second is {a**b}")