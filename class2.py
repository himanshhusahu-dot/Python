#strings

#indexing (positive,netagive)

#          0 1 2 3 4 5 6 7 8         positive
#          S H E R Y I A N S
#         -9-8-7-6-5-4-3-2-1         negative

name= "SHERYIANS"

print(name[4])        #it will print only letter Y.
print(name[2], name[-7])

#strings slicing

# print(name[start : stop : step])
# if we run slicing till 5 it will print to 4 only
# step mean 
# for value 1 it will cont print
# for 2 it will skip 1 word

print(name[0:4:1])




#type conversion/casting

# int() , str() , float() , bool()
# a= 12.5
# print(type(a))

a=12
print(float(a))