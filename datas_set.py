'''
SETS
1. Sets are annoted by {} or set()
    s = set()  --> empty set
2. Set stores only unique elements and remove the duplicates
    s = {1,1,2,2,3,4,5}
    will give output only {1,2,3,4,5}
3. Sets are unordered that means there is no indexing inside
4. Set are hectrogenous
5. Sets are semi- mutable
'''


# #List to set
# a = [1,1,2,2,3,4,5]
# print(set(a))


'''Sets Meathods'''

#1. .add()
# s = {1,2,3,4}
# s.add(5)
# print(s)



# 2. .remove()
# s = {1,2,3,4,5}
# s.remove(5)                 #enter element value in bracket, if element does not exist it will give error
# print(s)



# 3. .discard()
#same as remove but will not show any error if element is not in set




'''Sets Operations'''

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}


#1. .union()
#merge both set, take common element only one time

# print(f"union - {s1.union(s2)}")

#symbol for union --  
''' | '''
# print(s1 | s2)


#2. .intersection()

# print(f"intersection - {s1.intersection(s2)}")
#print common element from both set

#symbol for intersection -- 
''' & '''
# print(s1 & s2)



#3. .difference()
# elements present in one set but not in another

# print(f"difference - {s1.difference(s2)}")
# print(f"difference - {s2.difference(s1)}")

#symbol for diff is -- 
''' - '''
# print(s1-s2)



#4. .symmetric_difference()
#remove common element completly and merge two set
# print(f"symmetric dif - {s1.symmetric_difference(s2)}")

#symbol for symmetric diff --
''' ^ '''
# print( s1 ^ s2)






'''
|  Union
&  Intersection
-  Difference
^  Symmeritic Difference
'''

'''FROZENSET make any set with of fixed elements nither we cant add nor remove'''
# s = frozenset([1,2,3,4,5])
# s.add(6)           #it will give error
# print(s)



