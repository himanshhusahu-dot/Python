'''
Dictionary
1. Dictionary annoted by {curlt brackets}
2. Dictionary are combination of multiple key:values
3. Dictionary are mulables, can be cange the value by accessing their value. eg. d[3] = 100, it will change the value to 100 of 3rd key
4. dict are hectrogenous. 
5. in dict keys will be unique but value can be duplicates
6. dict are ordered.
'''
# d = {1:10, 2:20, 3:30}
# print(d[2])
#d[5] = 100       #we can create key:value pair which never exist
#print(d)



# for i in d:
#     print(i, d[i])             #i will print keys and d[i] will print values


'''
Meathods in dict
'''

#1. .keys()

# d = {"Ravi " : 80, "Rohan" : 23, "Devraj" : 88 }
# print(d.keys())

#2. .values()
# print(d.values())

#3. .items()
#it will give both keys and value 
# print(d.items())


#4. .pop()  -->enter key and it will remove both key and value
# d.pop("Rohan")
# print(d)
#it will remove the key and return the value if use in print



#5. .get()  --> agar key present h in dict so we will get value for that key otherwise None or ant messege when you write it comma lagane k baad
# print(d.get(5, "Not found"))



#6. .update() --> merge two dict
# a ={1:10,2:20,3:30}
# b = {4:40,5:50,6:60}
# a.update(b)
# print(a)





# d = {"ravi": 70, "abhishek" : 33, "Rohan" :12 }
# #M-1
# print(d.keys())

# #M2
# for i in d:
#     print(i)

# #M3
# for keys, value in d.items():
#     print(keys)






# d = {"ravi": 70, "abhishek" : 33, "Rohan" :12 }

# sum = 0
# for i in d:
#     sum +=d[i]

# print(sum)






# d = {"ravi": 70, "abhishek" : 33, "Rohan" :12 }
# for i in d:
#     if d[i]>50:
#         print(i)





# d = {"ravi": 70, "abhishek" : 88, "Rohan" :12 }

# max = 0
# name = ""
# for i in d:
#     if d[i]>max:
#         max = d[i]
#         name = i

# print(name)




# d = {"ravi": 70, "abhishek" : 88, "Rohan" :12 }

# for i in d:
#     print(d[i] + 5)


# d = {"ravi": 70, "abhishek" : 88, "Rohan" :12 }

# for i in d:
#     d[i] = d[i] + 5

# print(d)



'''
Practice Questions 12-10-25
'''

'''
**Q1. Create a Dictionary**

Create a dictionary containing your name, age, and city. Print the dictionary.

**Example Output:**

{'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
'''


# d = {"name" : "Himanshu", "age" : 20, "city" : "Jhansi"}
# print(d)



'''
**Q2. Access a Value**

Given a dictionary, print the value associated with the key "name".

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output: Rahul
'''

# d = {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}

# print(d["name"])



'''
**Q3. Add a New Key-Value Pair**

Add a new key "course" with value "Python" to the given dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20}
- Output: {'name': 'Rahul', 'age': 20, 'course': 'Python'}
'''


# d = {'name': 'Rahul', 'age': 20}

# d['course'] = "Python"
# print(d)

'''
**Q4. Update a Value**

Update the age of a person to 21.

**Example:**

- Input: {'name': 'Rahul', 'age': 20}
- Output: {'name': 'Rahul', 'age': 21}
'''

# d = {'name': 'Rahul', 'age': 20}

# d["age"] = 21
# print(d)



'''
**5. Delete a Key**

Remove the key "city" from the dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output: {'name': 'Rahul', 'age': 20}
'''

# d = {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}

# d.pop("city")
# print(d)





'''
**Q6. Check if a Key Exists**

Check whether the key "age" exists in the given dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20}
- Output: Key exists
'''


# d = {'name': 'Rahul', 'age': 20}
# a = input("enter - ")
# for i in d:
#     if a == i:
#         print("key exist")
#         break
# else:
#     print("key not exist")



'''
**Q7. Print All Keys**

Print all the keys present in a dictionary using a loop.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output:
name
age
city
'''




# d = {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
# for i in d:
#     print(i)



'''
**Q8. Print All Values**

Print all the values present in a dictionary using a loop.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output:
Rahul
20
Bhopal
'''

# d = {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
# for i in d:
#     print(d[i])



'''
**Q9. Count Key-Value Pairs**

Count the total number of key-value pairs in a dictionary without using len().

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 3
'''

# d = {'a': 10, 'b': 20, 'c': 30}
# count = 0
# for i in d:
#     count+=1

# print(count)



'''
**Q10. Calculate the Sum of Values**

Calculate the sum of all numerical values in a dictionary using a loop.

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 60
'''

# d = {'a': 10, 'b': 20, 'c': 30}
# sum = 0
# for i in d:
#     sum +=d[i]

# print(sum)



'''
Practice questions 16/10/26
'''

'''
Q1. Find the Largest Value
Given a dictionary containing numbers, find the largest value without using max().

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Output: 40
'''

# d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# max = 0
# for i in d:
#     if max< d[i]:
#         max = d[i]

# print(max)


'''
Q2. Find the Smallest Value
Given a dictionary containing numbers, find the smallest value without using min().

Example:
Input: {'a': 10, 'b': 25, 'c': 5, 'd': 40}
Output: 5
'''

# d ={'a': 10, 'b': 25, 'c': 5, 'd': 40}
# small = 0

# for i in d:
#     if small > d[i]:
#         small = d[i]
#     elif small ==0:
#         small = d[i]

# print(small)



'''
Q3 . Count Even and Odd Values
Count how many values in a dictionary are even and how many are odd.

Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}

Output:
Even: 2
Odd: 2
'''
# d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
# even = 0
# odd = 0
# for i in d:
#     if d[i] % 2 ==0:
#         even +=1
#     else:
#         odd+=1

# print(f"even - {even}")
# print(f"odd - {odd}")



'''
Q4.Sum of Even Values
Find the sum of all even values present in a dictionary.

Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}
Output: 30
'''

# d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
# sum = 0
# for i in d:
#     if d[i]%2==0:
#         sum += d[i]

# print(sum)



'''
Q5. Find a Key with a Given Value
Given a dictionary and a value, find the key associated with that value.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Value: 20
Output: b
'''

# n = int(input("enter"))
# d = {'a': 10, 'b': 20, 'c': 30}
# for i in d:
#     if d[i] == n:
#         print(i)




'''
Q6.Update All Values
Increase every value in a dictionary by 5.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Output: {'a': 15, 'b': 25, 'c': 35}
'''

# d = {'a': 10, 'b': 20, 'c': 30}
# for i in d:
#     d[i]+=5

# print(d)



'''
Q7.Count Values Greater Than a Number
Count how many dictionary values are greater than a given number.

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Number: 20
Output: 2
'''


# n= int(input("enter - "))
# count = 0
# d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# for i in d:
#     if d[i] >n:
#         count+=1
# print(count)




'''
Q8. Create a Dictionary from Two Lists
Given two lists, create a dictionary where the first list contains keys
and the second list contains values.

Example:
Keys: ['a', 'b', 'c']
Values: [10, 20, 30]

Output:
{'a': 10, 'b': 20, 'c': 30}
'''


# k = ['a', 'b', 'c']
# v = [10, 20, 30]
# d = {}

# for i in range(len(k)):
#     d[k[i]] = v[i]
# print(d)





'''
Q9.Count Values Equal to a Given Number
Given a dictionary and a number, count how many times that number
appears as a value in the dictionary.

Example:
Input: {'a': 10, 'b': 20, 'c': 10, 'd': 30}
Number: 10
Output: 2
'''



# n = int(input("Enter a numbre - "))
# d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
# count = 0
# for i in d:
#     if n == d[i]:
#         count+=1

# print(f"{n} is {count} times")





'''
Q10.Count Positive and Negative Values
Given a dictionary containing numbers, count how many values are
positive and how many are negative.

Example:
Input: {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}

Output:
Positive: 3
Negative: 2
'''


# d = {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}
# pos = 0
# neg = 0
# for i in d:
#     if d[i]>0:
#         pos +=1
#     elif d[i]<0:
#         neg +=1

# print(f"positive - {pos}")
# print(f"negative - {neg}")




