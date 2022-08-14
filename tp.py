#Q1
#Write a Python program to create a tuple.

from typing import Tuple


a = (1,4)
print(a)
print(type(a))


#Q2
#Write a Python program to create a tuple with different data types.

tple = (1,1.4, True, "acpatil")
print(tple)

#Q3
#Write a Python program to unpack a tuple in several variables.

a = 5,6,7
x1,x2,x3= a
print(a)
print(x1+x2+x3)




#Q4
# Write a Python program to create the colon of a tuple.
from copy import deepcopy
tt = (1,"acpatil",[],55)
print(tt)
cc = deepcopy(tt)
cc[2].append(20)
print(cc)
print(tt)

#OR

tt = (1,"acpatil",2 ,[],55)
print(tt)
cc = list(tt)
cc[3].append(50)
print(cc)
print(tt)

#Q5
#Write a Python program to find the repeated items of a tuple

gg = (1,2,3,4,5,4,5,5,5,5,6,8,7,9,8,9)
dd = gg.count(9)
print(dd)

#Q6
# Write a Python program to check whether an element exists within a tuple.
a = ("string", 1,5, 2, 3, 5, 6, 8 )
print("r" in a)
print(8 in a)
#Q7
#Write a Python program to convert a list to a tuple.

do = [1,2,3,4,5,6,7,8,9]
df = tuple(do)
print(do)
print(df)

#Q8
#Write a Python program to remove an item from a tuple.

ccc = (1,2,3,4,5,6,8,6,9)
ddd = list(ccc)
print(ccc)
ddd.remove(ccc[8])
print(ddd)


#Q9
#Write a Python program to slice a tuple.

a =(1,2,3,4,5,6,7,8,9)
bb = a[5:9]
print(bb)

#10
#Write a Python program to reverse a tuple.
tt = (1,2,3,4,5,6,7,8,9)
print(tt[::-1])
