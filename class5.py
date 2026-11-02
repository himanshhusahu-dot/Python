#control flow statement
#if else

# age = int(input("Enter ur age - "))
# if age>=18:
#     print("u can vote")
#     print("thankyou visit again")
# else:
#     print("you can not vote")

#elif

# money= int(input("What is the value - "))
# if money==100:
#     print("sandwich")
# elif money== 200:
#     print("biryani")
# else:
#     print("handi biryani")

# a= int(input("1st number= "))
# b= int(input("2nd number = "))

# if a>b:
#     print("1st is greater")
# else:
#     print("2nd is greater")



# a= (input("Enter ur gender(M/F)-"))
# if a=="M" or a=="m":
#     print("hi sir ")
# else:
#     print("hi madam")



#Practice sheet if else : 24/9/26

# Q1) take input of a number and check wheather it is negative or positive

# a= int(input("Enter the number : "))
# if a>0:
#     print(f"{a} is positive")
# elif a==0:
#     print(f"{a} nither positive nor negative")
# else:
#     print(f"{a} is negative")


# Q2)  check whether even or odd

# a= int(input("Enter number : "))
# if a%2==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")


# Q3)  input of 2 number and check the greatest

# a= int(input("Enter the 1st number : "))
# b= int(input("Enter the 2nd number : "))
# if a>b:
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")

# Q4)  take input of 2 numbers and check weather they are equal or not

# a= int(input("Enter the 1st number : "))
# b= int(input("Enter the 2nd number : "))
# if a==b:
#     print(f"{a} and {b} are equal")
# else:
#     print(f"{a} and {b} are not equal")

#Q5)  If marks more than or equal to 40 then pass 
# a= int(input("Enter the marks : "))
# if a>=40:
#     print("you are pass")
# else:
#     print("you are fail")







# check if an alphabet is vovel or consonant.

# a= str(input("Enter the alphabet: "))
# if a== "a" or a== "e" or a=="i" or a=="o" or a== "u":
#     print{f"{a} is vowel"}
# else:
#     print(f"{a} is consonant")






# in operator code can also writter as this if we does not want to write or again again 

# line 91 
# if a in "aeiouAEIOU":






''' take input of 3 sub and syudents should get atleast 40 marks in every sub then he is pass'''

# maths= int(input("Enter maths marks - "))
# science = int(input("Enter science marks - "))
# english = int(input("Enter english marks - "))
# if maths >= 40 and science>= 40 and english >= 40:
#     print("pass")
# else:
#     print("fail") 








'''take a number from the user 
if the number is even
check wheather it is disible by 4
if not print odd'''

# a= int(input("Enter the number : "))

# if a%2==0:
#     print("Number is even")
#     if a%4==0:
#         print("Number is disible by 4")
#     else:
#         print("Number is not disible by 4")
# else:
#     print("number is oddd")






'''ATM withdrawl
assume correct pin is 1234
and the acc balance is $5000

ask the user to enter the pin
if the pin is correct, ask them to enter the withdrawl ammount
if the withdrawl amount is less than the acc balane then show sucess
otherwise failure'''


# pin = int(input("Enter the pin : "))

# if pin==1234:
#     amount= int(input("Enter the withdrawl amount : "))
#     if amount<=5000:
#         print("Withdrawl Sucessfull")
#     else:
#         print("Balance low")
# else:
#     print("invalid Pin")







'''Take a num from thr user
if it is positive 
check wether it is even or odd
if the number is even 
check wether it is disible by 4 or not
'''

# num = int(input("Enter the number : "))

# if num>0:
#     if num%2==0:
#         print("Number is even")
#         if num%4==0:
#             print("Number is disible by 4")
#         else:
#             print("Number is not disible by 4")
#     else:
#         print("Number is odd")
# else:
#     print("Number is Negative")





# a= int(input("Enter the first number : "))
# b= int(input("Enter the secon dnumber : "))

# if a>b:
#     print("First number is greater")
#     if a%2==0: 
#         print("First number is even")
#     else:
#         print("First number is odd")
# else:
#     print("Second number is greater")
#     if b%2==0:
#         print("Second number is even")
#     else:
#         print("Second number is odd")





# Practice Questions

#Q1)
# a= int(input("Enter the first number : "))
# b= int(input("Enter the second number : "))

# if a>0:
#     if a>b:
#         print("first number is greater than the second number")
#     else:
#         print("second number is greater")
# else:
#     print("First numer is negative")


#Q2) 

# a= int(input("enter the marks of first sub : "))
# b= int(input("enter the subject of second sub : "))

# if a>= 33:
#     if b>=33:
#         print("Pass")
#     else:
#         print ("fail")
# else:
#     print("fail")


# Q3 ) 

# a= int(input("Enter age : "))
# b= int(input("permission : "))

# if a>=18:
#     if b==1:
#         print("Allowed")
#     else("Permision Requried")
# else:
#     print("Under Age")



#Q4)
# a= int(input("Enter the first number : "))
# b= int(input("Enter the second number : "))

# if a==b:
#     print("Both num r equal")
# else:
#     if a>b:
#         print("First number is greater")
#     else:
#         print("Second number is greater")




#Q5 )

# am= int(input("Enetr the shopping amount"))
# m= int(input("Enter the membership status (1 for yes and 0 for no) : "))

# if m==1:
#     if am>=1000:
#         print("Discount not availble")
#     else:
#         print("Discount not availble under 1000")
# else:
#     ("you are not a member")