'''
Armstrong Number
'''

## check if 153 is armstrong
# #1**3 = 1
## 5**3 = 125
## 3**3 = 27

## add 1+125+27 = 153 


n = int(input("Enter a number - "))
sum = 0 
temp = n                                                 #take a temperory variable becoz in last when u compare in if condition with n (n=0)
length = len(str(n))                       #find length of n, lenght can be find of string
while n>0:
    last = n%10 
    sum = sum + last**length             # ** length
    n = n//10
print(sum)
if temp == sum:
    print("number is armstrong")
else:
    print("number is not armstrong")



