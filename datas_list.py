'''
Lists
1. square Brackets[]
2. Hectrogenous data structure(can store diffrent type of data type together)
3. allow storing duplicate values
4. lists are ordered because they have indexing and indexing starts from 0
5. lists are mutable -> we can change any value any time
'''

# marks = []   #empty list

# marks = [90,9,46,34,66,90,34,"Himanshu", 3.14, True, 2+8j]
# # print(marks)
# # print(marks[3])           #indexing(starts from 0), it will print 34
# print(marks[1:5])         #slicing starting index(1) and stop index(5)

#if want to change anything in list
# marks[3] = "abcd"                    #this will change 34 (indexing = 3) to abcd


'''Traversing
'''

#jab list k har element k ps ja kr use print krte h to use traversing bolte h
# a = [10,20,30,40,50]
# for i in a:
#     print(i)




'''agr kisi keyword k aage '.' hai to woh MEATHOD hoga aur agr nhi h to woh function hoga'''


#Meathod in LIST
#1.  .append() 

# add the value at the last of the list. buyt only add 1 value
# marks=[10,20,30,40,50]
# marks.append(60)
# print(marks)        #this will add 90 to last after 50


#2. .extend()

# marks2 = [70,80,90]
# marks.extend(marks2)
# print(marks)



# marks2.extend(marks)
# print(marks2)




#3. .insert()

#.insert(index, value)

# marks.insert(3 , 35)
# print(marks)




#4. .remove()

#enter the value inside the bracket and it will remove the first ocuring value from list
# a = [10,20,30,40,50,10,60]
# a.remove(10)
# print(a)




#5. .pop

#remove any value on basis of index if not given index then it will remove last value
# a=[10,20,30,40,50,60]
# a.pop(3)
# print(a)



#6. .clear
#remove all the element from the list
# a=[10,20,30,40,50]
# a.clear
# print(a)



#7. del
#remove the list completlyfrom memory
# a=[10,20,30,40,50,60]
# del a 
# print(a)




'''
Shallow Copy
'''

# a= [1,2,3,4,5]
# b= a
# b[3] = 100
# print(a)
# print(b)

#this will change in both

'''
Deep Copy
'''

# a= [1,2,3,4,5]
# b= a.copy()
# b[3] = 100
# print(a)
# print(b)

#this will change only in b

'''-----------------------------------------------------------------------------------------------------------------------------------'''
#print indexing with their number
# lr=[]
# l = [10,20,30,40,50,60,70,80]
# for i in range(len(l)-1,-1,-1):
#     lr.append(l[i])

# print(lr)


'''
List practice sheet 10/10/26
'''


'''Q1. Find the Smallest Element

Create a list of numbers and find the smallest element without using the min() function.

Example:

Input: [12, 5, 23, 8, 17]

Output: 5'''

# small = 0
# a = [10,12,5,23,54,17]
# for i in a:
#     if i<small:
#         small = i
#     elif small ==0:
#         small = i

# print(small)


'''Q2. Count Positive and Negative Numbers

Create a list and count the number of positive and negative elements. Ignore zeros.

Example:

Input: [10, -5, 20, -8, 0, 7]

Output:

Positive: 3
Negative: 2'''

# l = []
# element = int(input("Enter number of element in list :- "))
# for i in  range(1,element+1):
#     a = int(input("Enter a number :- "))
#     l.append(a)

# neg = 0
# pos = 0
# for i in l:
#     if i>0:
#         pos+=1
#     elif i<0:
#         neg+=1
# print(f"Positive : {pos}")
# print(f"Negative : {neg}")



'''Create a list of numbers and calculate the average of all its elements.

Example:

Input: [10, 20, 30, 40]

Output: 25.0'''

# a = [10,20,30,40]
# l = len(a)
# sum = 0
# for i in a:
#     sum+=i

# print (f"average is {sum/l}")



'''Q4. Count Occurrences of an Element

Create a list and count how many times a given number appears in it.

Example:

Input: [2, 4, 2, 6, 2, 8]

Number: 2

Output: 3'''

# l = [2,4,2,6,2,8]
# count = 0
# num = int(input("Enter a number :- "))
# for i in l:
#     if i == num:
#         count+=1

# print(f"{num} is {count} times")





'''Q5. Print Elements at Even Indices

Create a list and print the elements present at even indices (0, 2, 4, …).

Example:

Input: [10, 20, 30, 40, 50, 60]

Output: [10, 30, 50]'''

# l = [10,20,30,40,50,60]
# p = []
# leng = len(l)
# for i in range(0,leng):
#     if i%2==0:
#         p.append(l[i])

# print(p)






'''Q6. Find the Second Largest Element

Create a list and find the second largest distinct element without using sort() or max().

Example:

Input: [10, 25, 15, 40, 30]

Output: 30'''

# l = [10,25,15,40,30]
# great = 0
# great2 = 0
# for i in l:
#     if i >great:
#         great = i

# for i in l:
#     if i>great2 and i != great:
#         great2 = i

# print(great2)






'''Q7. Replace Negative Numbers with Zero

Create a list and replace every negative element with 0.

Example:

Input: [10, -5, 20, -8, 7]

Output: [10, 0, 20, 0, 7]'''

# l = [10,-5,20,-8,7]
# for i in range(0,len(l)):
#     if l[i]<=0:
#         l[i] = 0

# print(l)





'''Q8. Find the Sum of List Elements

Create a list of numbers and calculate the sum of all its elements.

Example:

Input: [10, 20, 30, 40]

Output: 100'''

# l = [10,20,30,40]
# sum = 0
# for i in l:
#     sum+=i

# print(sum)





'''Q9. Find the Largest Element

Create a list of numbers and find the largest element without using the max() function.

Example:

Input: [12, 45, 23, 67, 34]

Output: 67'''

# l = [10,45,23,67,34]
# lar = 0
# for i in l:
#     if i>lar:
#         lar =i
# print(lar)



'''Q10. Reverse a List

Create a list and reverse its elements without using the reverse() method.

Example:

Input: [10, 20, 30, 40, 50]

Output: [50, 40, 30, 20, 10]'''


# l = [10,20,30,40,50]
# lr = []
# for i in range(len(l)-1,-1,-1):
#     lr.append(l[i])

# print(lr)



'''
Print list element in reverse order
reverse the list order using the two-pointer approach
'''

# a = [10,20,30,40,50]
# n = len(a)
# for i in range(0,len(a)//2):
#     a[i] , a[n-i-1] = a[n-i-1] , a[i]

# print(a)




'''print negative and postive number, ignore 0'''

# arr = [10,-5,20,-3,0,8]
# print("positive")
# for i in arr:
#     if i>0:
#         print(i)

# print("Negative")

# for i in arr:
#     if i<0:
#         print(i)



'''print average'''

# a = [10,20,30,40]
# len = len(a)
# sum = 0
# for i in a:
#     sum +=i

# print(sum/len)






# '''print maximum number and also its index'''

# a = [2,96,69,77,145,20]
# max = 0
# ind = 0
# for i in range(0,len(a)):
#     if max<a[i]:
#         max = a[i]
#         ind = i

# print(f"Maximum number is {max}")
# print(f"found at index {ind}")



'''List practice questions 12/10/26'''




'''**Q1. Separate Even and Odd Numbers**

Create a list of integers and separate the even and odd numbers into two different lists.

**Example:**

- Input: [1, 2, 3, 4, 5, 6]
- Output:
    - Even: [2, 4, 6]
    - Odd: [1, 3, 5]'''

# a= [1,2,3,4,5,6]
# even = []
# odd = []
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(f"even - {even}")
# print(f"odd - {odd}")



'''**Q2. Remove Duplicates**

Create a list and remove duplicate elements without using set().

**Example:**

- Input: [1, 2, 3, 2, 4, 1, 5]
- Output: [1, 2, 3, 4, 5]'''

# a =[1, 2, 3, 2, 4, 1, 5]
# b = []

# for i in a:
#     count = 0
#     for j in b:
#         if i == j:
#             count +=1

#     if count ==0:
#         b.append(i)

# print(b)





            



'''
**3. Find the Index of an Element**

Create a list and find the index of a given element without using the index() method.

**Example:**

- Input: [10, 20, 30, 40, 50]
- Element: 30
- Output: 2
'''


# a = [10,20,30,40,50]
# n = int(input("enter number - "))
# ind = 0
# for i in range(0,len(a)):
#     if n == a[i]:
#         ind = i
# print(ind)



'''
**Q4. Swap First and Last Elements**

Create a list and swap its first and last elements.

**Example:**

- Input: [10, 20, 30, 40, 50]
- Output: [50, 20, 30, 40, 10]
'''

# a = [10,20,30,40,50]
# rev = []
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])

# print(rev)




'''
**Q5. Find the Second Smallest Element**

Find the second smallest distinct element without using sort() or min().

**Example:**

- Input: [15, 5, 20, 8, 12]
- Output: 8
'''

# a = [15,5,20,8,12]
# min = 0
# min2 = 0
# for i in a:
#     if min>i:
#         min = i
#     elif min ==0:
#         min = i

# for i in a:
#     if min2>i and min != i:
#         min2 = i
#     elif min2 == 0:
#         min2 = i

# print(min2)


'''
**Q6. Multiply All Elements**

Create a list and calculate the product of all its elements.

**Example:**

- Input: [2, 3, 4, 5]
- Output: 120
'''


# a = [2,3,4,5]
# pro = 1
# for i in a:
#     pro*=i

# print(pro)





'''
**Q7. Count Numbers Greater Than a Given Value**

Create a list and count how many elements are greater than a given number.

**Example:**

- Input: [10, 25, 15, 40, 30]
- Number: 20
- Output: 3
'''

# n = int(input("ent num - "))
# a = [10,25,15,40,30]
# count = 0
# for i in a:
#     if i>n:
#         count+=1

# print(count)




'''
**Q8. Count Numbers Smaller Than a Given Value**

Create a list and count how many elements are smaller than a given number.

**Example:**

- Input: [10, 25, 15, 40, 30]
- Number: 20
- Output: 2
'''

# n = int(input("ent num - "))
# a = [10,25,15,40,30]
# count = 0
# for i in a:
#     if i<n:
#         count+=1

# print(count)




'''
**Q9. Merge Two Lists**

Merge two lists into a single list without using the + operator.

**Example:**

- Input: [1, 2, 3] and [4, 5, 6]
- Output: [1, 2, 3, 4, 5, 6]
'''

# a = [1,2,3]
# b = [4,5,6]

# a.extend(b)
# print(a)
'''-----------------------------'''

# for i in b:
#     a.append(i)

# print(a)



'''
**Q10. Print Elements at Odd Indices**

Print all elements present at odd indices (1, 3, 5, …) of a list.

**Example:**

- Input: [10, 20, 30, 40, 50, 60]
- Output: [20, 40, 60]
'''


# a = [10,20,30,40,50,60]
# l = []
# for i in range(0,len(a)):
#     if i%2!=0:
#         l.append(a[i])

# print(l)





# a = [1,2,4,5]
# sum = 0

# for i in a:
#     sum+=i

# realsum = ((len(a)+1)*((len(a)+2))//2)               #here we take the total no of element in list will bw len(a)+1, becoz 1 no is misssing
# # this is formula of sum upto n generated by AP
# print(f"missing value is {realsum - sum}")


'''
check if list is arrenged in accending order
'''

# a = [10,20,30,40,50]
# leng = len(a)
# cond = False
# for i in range(0,leng-1):
#     if a[i]<a[i+1]:
#         cond = True

# if cond == True:
#     print("sorted")
# else:
#     print("not sorted")





'''
Check pallindromic list
'''

# a = [2,3,15,15,3,2]
# leng = len(a)
# cond = True
# for i in range(0,leng//2):
#     if a[i] != a[leng-i-1]:
#         cond = False

# if cond == True:
#     print("Pallindrome list")
# else:
#     print("Not pallindrome list")




