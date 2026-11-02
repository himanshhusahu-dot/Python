'''
Jb tk condition true ni hogi tb tk loop chlega
Jb condition false hogi tb loop rukega
'''




'''
print 1 -10 using while loop
'''
# i=1
# while i <= 10:
#     print(i)
#     i +=1




'''
print 10 - 1
'''
# i = 10
# while i>=1:
#     print(i)
#     i-=1



'''
take input password
'''
# a= ""
# while a != "hs":
#     a=input("Enter your password - ")
# print("Acess Granted")




'''
Table of any number
'''
# n = int(input("Enter a number - "))
# i = 1
# while i<=10:
#     print(n*i)
#     i +=1




'''
print even number from 1-20
'''
# i = 2
# while i<=20:
#     print(i)
#     i+=2


'''
print sum of even number
'''
# i=2
# sum = 0
# while i<=20:
#     sum = sum + i
#     i +=2
# print(sum)



'''
print a number in revesse order
'''
# n=1234
# while n != 0:
#     print(n%10)
#     n = n // 10



'''print in same line
'''
# n = 1234
# a = 0
# while n!=0:
#     last = n%10
#     a = a*10 + last 
#     n = n//10
# print(a)




'''
how many digit in the number
'''
# n = int(input(""))
# a = 0
# count = 0
# while n!=0:
#     a = n%10
#     count +=1
#     n = n//10
# print(count)



'''
Practice Questions  2-10-26
'''

#Q1) 

'''using while loop'''
# n= int(input("Enter a number - "))
# i = 1
# odd = 0
# while i<=n:
#     odd = odd+i
#     i+=2

# b = 2
# even = 0
# while b<=n:
#     even = even + b
#     b+=2

# if even > odd:
#     print(even - odd)
# else:
#     print(odd - even)




'''using for loop'''
# even = 0
# odd = 0
# for i in range(2,n+1,2):
#     even+=i
# for i in range(1,n+1,2):
#     odd+=i
# if even > odd:
#     print(even - odd)
# else:
#     print(odd - even)



#Q2) 
# n = int(input("Enter how many number - "))
# i = 1
# big = 0
# small = int(input("Enter a number - "))           #first input yaha lelo kyuki loop start krne k liye kch valur chaiye
# while i<=(n-1):
#     a = int(input("Enter a number - "))
#     if a>big:
#         big = a 
#     if small>big:                            #first input ko bi compare krenge
#         big = small
#     if a<small:
#         small = a
#     i+=1
# print (f"smallest is {small}")
# print(f"biggest is {big}")
# print(f"diffrence is {big - small}")




#Q3)
# n = int(input("Enter how many numbers - "))
# i = 1
# z = int(input("Enter a number - "))
# while i<=(n-1):
#     a = int(input("Enter a number - "))
#     if a<z:
#         z=a
#     i+=1
# print(z)





'''G'''

# n = int(input("Enter n: "))

# i = 0

# while i < n:
#     num = int(input("Enter number: "))

#     if i == 0:
#         smallest = num
#     elif num < smallest:
#         smallest = num

#     i += 1

# print("Smallest =", smallest)



#Q4)
# count = 0
# for i in range(1,7):
#     a= int(input("Enter number - "))
#     if a%10 ==0:
#         count+=1
# print(count)



#Q5)
# n= int(input("Enter number - "))
# count = 0
# i = 1
# while i<=n:
#     if i%5==0 and i%10!=0:
#         count+=1
#     i+=1
# print(count)




#Q6)
# n = int(input("Enter number - "))
# a = n%10
# last = 0
# z = 0
# while n%10!=0:
#     z = n%10
#     last = last*10 + z
#     n= n//10

# b = last%10
# if a==b:
#     print("same")
# else:
#     print("diffrent")






'''Practice Question 03-10-26'''
#Q1)
# n = int(input("Enter a number - "))
# last = 0
# while n>0:
#     a = n%10
#     last = last*10 + a
#     n = n//10
# print(last)


#Q3)
# count = 0
# n = int(input("Enter a number - "))
# while n>0:
#     a = n%10
#     n = n//10
#     if a>=5:
#         count = count +1
# print(count)


#Q4) 
# n = int(input("Enter a number - "))
# multi = 1
# while n>0:
#     a = n%10
#     n = n//10
#     multi = multi*a
# print(multi)


#Q5)
# n = int(input("Enter a number - "))
# while n>0:
#     a = n%10
#     n = n//10
#     if a==7:
#         print("present")
#     else:
#         print("not present")


#Q6)
# n = int(input("Enter a number - "))
# count = 0
# while n>0:
#     a = n%10
#     n = n//10
#     if a%3==0:
#         count = count +1
# print(count)

#Q7)
# n= int(input("Enter a number - "))
# x = 0
# while n>0:
#     a = n%10
#     n = n//10
#     x = x*10 + 9
# print(x)


#Q8)
# n = int(input("Enter a number - "))
# big = 0
# big2 = 0
# while n>0:
#     a = n%10
#     n = n//10
#     if a>big:
#         '''big2 = big'''                                       #this can also be written insteed of 2nd if condition
#         big = a
#     if a>big2 and a!=big:
#         big2 = a
# print(f"Second largest is {big2}")



#Q9)
# n = int(input("Enter a number - "))
# count = 0
# length = len(str(n))
# while n>0:
#     a = n%10
#     n = n//10
#     if a%2==0:
#         print("Yes")
#         break
#     if a%2!=0:
#         count+=1
#     if count == length:
#         print("No")



#Q10)
# n= int(input("Enter a number - ")) 
# a = 0
# while n>0:
#     n = n//10
#     break
# print(n)
