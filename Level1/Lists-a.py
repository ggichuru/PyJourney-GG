### LIST this is a data structure in python whose values are encapsulated in square brackets
   # and seprated by commas. A list is mutable 

from typing import List


List1 = [0,1,2,3,4,5,6,7,8,9]

print(List1[2:7])

# concatenation
List2 = [10, 11, 12, 13, 14, 15, 16, 18, 19, 20]
List3 = List1 + List2
List4 = [['Alex', 'Ian', 'Ben'], [10, 20, 30,]]    ## Multidimensional Lists
print(List3)
print(List4)

# Mutability 
List1[4] = 33
print(List1)

## Add items at the end using append() method.
List2.append('appended')
print(List2)
List4.append((78,-1))  #add a tupple to a list
print(List4)

# Built in function
   # len() length of list
print(len(List2))

# Nesting Lists
x = ['a', 'b', 'c']
y = [1,2,3]
z = ['Alex', 34, 'Brian', 23]
a = [x,y,z]
print(a)

