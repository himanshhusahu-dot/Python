'''
how functions are created
'''
#1) inbuilt
# print()
# input()
# len()
# int()
# float()
# etc 



#2) user defined functions

#defining a function
# def hello():
#     print("How are you")

#callig a function
# hello()


'''return'''

# def hey():
#     return "How are you"        #return the value to the calling block

# a = hey()   #calling block captures the value
# print(a)
'''OR'''
# print(hey())



'''Parameters and Arguments'''

# def addition(a,b):         #taking parameter
#     print(a+b)

# addition(10,10)       #provide arguments


'''Check palindrome from 1 to 1000'''

# def palindrome(a):
#     rev = 0
#     copy = a
#     while a!=0:
#         rev = rev*10 +a%10
#         a= a//10

#     if copy ==rev:
#         print(copy)


# for i in range(1,1000):
#     palindrome(i)

'''Practice questions 5/10/26'''

#Q1)

# def add(a,b):
#     return(a+b)

# print(add(10,20))


#Q2)

# def check_even_odd(a):
#     if a%10==0:
#         return("even")
#     else:
#         return("odd")

# print(check_even_odd(7))

#Q3)

# def square(a):
#     return(a**2)

# print(square(6))

#Q4)

# def maximum(a,b):
#     if a>b:
#         return(a)
#     else:
#         return(b)

# print(maximum(12,25))

#Q5)

# def check_number(a):
#     if a>0:
#         return("Positive")
#     elif a<0:
#         return("negative")
#     else:
#         return("0")

# print(check_number(-8))

#Q6)

# def simple_intrest(P,R,T):
#     return((P*R*T)/100)

# print(simple_intrest(1000,5,2))

#Q7)

# def cube(a):
#     return(a**3)

# print(cube(4))

#Q8)

# def eligible(a):
#     if a>18 or a == 18:
#         return ("eligible")
#     else:
#         return("Not eligible")

# print(eligible(20))

#Q9)

# def factorial ():
#     a = int(input("Enter a number - "))
#     fac = 1
#     for i in range(1,a+1):
#         fac = fac*i
#     return(fac)

# print(factorial())

#Q10)

# def count_digit():
#     a = int(input("Enter a number - "))
#     count = 0
#     while a!=0:
#         last = a%10
#         count+=1
#         a = a//10
#     return(count)

# print(count_digit())


'''Defaults parameter'''
# def hello(a, b = 10):   #b is default value, if you enter b it will reassing and if not it will be 10 
#     print(a+b)

# hello(2)       #12
# hello(2,20)          #22



'''Default arguments'''

# def informations(name, age, number):
#     print("Hello your information is ")
#     print(name)
#     print(age)
#     print(number)

# informations(age = 20, number = 8810769745, name = "Himanshu")    #agruments can be given here also



'''print number from 1 to 30
cant use loop and cant use print more than once'''

# def numbers(n):
#     if n==30:
#         return                 #here we will use return to stop function
#     print(n)
#     numbers(n+1)               #we can use function inside that same function

# numbers(1)


'''STACK'''

# def hello1():
#     hello2()
#     print("hello1")                             #after executing hello1 function it will execute hello2 then hello3 then hello4
                                                
# def hello2():                                   #and it will stote print command into stack and will run as last in first out
#     hello3()                                    #so it will print hello3 after hello4
#     print("hello2")

# def hello3():
#     hello4()
#     print("hello3")

# def hello4():
#     print("hello4")

# hello1()




# def numbers(n):                             #same concept of stack in this also.. it will print reverse order from 30 to 1
#     if n ==31:
#         return
#     numbers(n+1)
#     print(n)
#     numbers(1)




'''Practice questions 6/10/26'''

# #Q1. Find the Largest of Three Numbers
# Create a function largest() that takes three numbers and returns the largest number.

# Example:
# Input: 12 45 23
# Output: 45


# def largest(a,b,c):
#     d = 0
#     if a>b:
#             d = a
#     elif b>a:
#         d = b
#     if d>c:
#          return(d)
#     else:
#          return(c)

# print(largest(12,45,23))



#Q2. Check Prime Number
# Create a function is_prime() that takes a number and returns "Prime" if the number is prime, otherwise returns "Not Prime".

# Example:
# Input: 17
# Output: Prime


# def is_prime(a):
#     for i in range(2,a):
#         if a%i==0:
#             return("Not Prime")
#         else:
#             return("Prime")

# print(is_prime(17))




#Q3. Sum of Digits
# Create a function sum_of_digits() that takes a number and returns the sum of its digits.

# Example:
# Input: 12345
# Output: 15


# def sum_of_digit(a):
#     sum = 0
#     while a !=0:
#         last = a%10
#         sum+=last
#         a = a//10
#     return(sum)

# print(sum_of_digit(12345))


#Q6) 
# def gcd():
#     a = int(input("Enter a number - "))
#     b = int(input("Enter a number - "))
#     result = 0
#     for i in range(1,a+1):
#         if a%i==0 and b%i==0:
#             result = i
#     return(result)

# print(gcd())


nums = [1,5,0,3,5]
count = 0
while True:        
    min = 0
    copy = nums
    for i in nums:
        if i > min:
            min = i

    for i in nums:
        if i < min and i !=0:
            min = i
    if min == 0:
        break
            
    for i in range(len(copy)):
        if copy[i] !=0:
            copy[i]-=min
        count +=1
            
    
print(count)






