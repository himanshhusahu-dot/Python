# automating a task
# a = range(1 , 6 , 1)

# for i in a:
#     print("hello world")


# this will print hello worls 5 times

# for i in range(1, 6, 1):
#     print("Hello world")

# this will also print same thimg

#Q1)   range to -80

# for i in range(10 , 81 , 1):
#     print(i)

#Q2) range -52 to -39

# for i in range(-52 , -40 , 1):
#     print(i)

#Q3) 100 to -100

# for i in range (100, -101, -1):
#     print(i)


#Q4) table of 7

# for i in range(7,75,7):
#     print(i)


#Q5) table of any number

# n = int(input("Enter the number : "))

# for i in range (n , ((n*10))+1, n):
#     print(i)


#Practice Questions for loops 29-09-26

#Q1) 
# a= int(input("Enter the number"))

# for i in range(1,a+1,1):
#     print(i)


#Q2) 
# n=int(input("Enter the number - "))

# for i in range(n,0,-1):
#     print(i)

#Q3)
# n=int(input("Enter the number"))

# for i in range(1,n+1,2):
#     print(i)


#Q4)
# n=int(input("Enter the number - "))

# for i in range(2,n+1,2):
#     print(i)

#Q5) 
# n=int(input("Enter the number - "))

# for i in range(n,n*10+1, n):
#     print(i)

#Q8)
# n=int(input("Enter the number - "))

# for i in range(1,n+1,1):
#     print(i**2)

#Q6)
# n= int(input("Enter the number - "))

# for i in range(1,n+1,1):
#     print()



'''take an input n and print natural numbers upto n'''

# n= int(input("Enter the number "))

# for i in range(1,n+1,1):
#     print(i)





'''print from n to 1'''

# n= int(input("Enter your number "))
# for i in range(n,0,-1):
#     print(i)


'''sum of number'''

# n= int(input("Enter the number "))
# sum = 0
# for i in range(1,n+1,1):
#     sum = sum +i

# print(sum)




'''factorial'''


# n = int(input("Enter the number :- "))
# fac = 1

# for i in range(1,n+1):
#     fac = fac*i

# print(fac)


'''factors'''

# n= int(input("Enter the number :- "))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)



#practice Question 01-10-26

#Q1) 

# present = 0
# absent = 0
# for i in range (1,8,1):
#     a = input("Enter attendance :- ")
#     if a == "P" or a == "p":
#         present = present+1
#     else:
#         absent = absent+1

# print(f"Total present is {present}")
# print(f"Total absent is {absent}")



#Q2) 

# passs = 0
# fail = 0

# for i in range (1,11):
#     a= int(input("Enter Condition check (1 for pass and 0 for fail) :- "))
#     if a==1:
#         passs = passs+1
#     elif a==0:
#         fail = fail+1

# print(f"inspection pass {passs}")
# print(f"inspection fail {fail}")




#Q3) 

# save = 0
# for i in range(1,8):
#     a = int(input("Enter the saving amount :- "))
#     if a>= 500:
#         save = save+1

# print(f"Total saving is {save}")



# #Q4) 

# unit = 0
# z=0
# for i in range(1,8):
#     a= int(input("Enter the consume units :- "))
#     z = z+a
#     if a>=10:
#         unit = unit + 1

# print (unit)
# print(z)


#Q5) 

# present = 0
# absent = 0

# for i in range(1,11):
#     a= input("Enter attendance :- ")
#     if a== "p" or a=="p":
#         present = present +1
#     else:
#         absent = absent +1

# print(f" total present in percent is {present*10} %")

# if present*10 >=75:
#     print("attendance is more than 75%")
# else:
#     print("attendance is not more than 75%")

# count = 0
# a = int(input("Enter the number"))
# for i in range(1,6):
#     if a%i==0:
#         count= count+1                                  #also can be written as count += 1
# print(count)

#for prime number

#if count ==2:
    #print(f"{a} is a prime number")
#else:
     #print(f"it is not")




'''break operator'''

# n = int(input("Enter the number "))
# for i in range(2,n):                      #remove 1 and 5 (if n=5) becoz they are also factor
#     if n%i==0:
#         print(f"{n} is a composite number")
#         break                                        #use break to end program, if u will not then it will run program every time for every value of i and print multiple time
#     else:
#         print(f"{n} is a prime number")






# name = "AbhiSHEK"
# upper = 0
# lower = 0

# for i in name:
#     if i.isupper():
#         upper +=1
#     elif i.islower():
#         lower +=1

# print(f"upper is {upper}")
# print(f"lower is {lower}")





prices = [7, 1, 5, 3, 6, 4]
copy = prices
copy.pop(0)
print(prices)