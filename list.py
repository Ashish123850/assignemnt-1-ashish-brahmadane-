
#list

#Q1
#Write a Python program to sum all the items in a list

from ast import Mult
from audioop import mul
from math import prod


value = [1,2,3,4,5]
a = sum(value)
print(a)

#Q2
#Write a Python program to multiplies all the items in a list.

value = [1,2,3,4,5]
b = prod(value)
print(b)

#Q3
#Write a Python program to get the smallest number from a list.
a = [6,2,5,8,6,9]
print(min(a))

#Q6
#Write a Python program to remove duplicates from a list.
import itertools
from re import T
aaa = [1,2,5,1,6,5,2,6,3]
aaa.sort()
new = list(aaa for aaa,_ in itertools.groupby(aaa))
print(new)

#Q7
#Write a Python program to clone or copy a list.
dd = [1,2,3,5,6,4,9]
bb = list(dd)
print(bb)



#Q8
#Write a Python program to find the list of words that are longer than n from a
#given list of words

def words(n, str):
    word = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word.append(x)
    return word	
print(words(3, "The cat run out of the door because she like to rome outside"))


#Q10
#Write a Python program to print a specified list after removing the 0th, 4th and
#5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

ff = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

unwanted =[0,4,5]
for i in sorted(unwanted, reverse=True):
    del ff[i]
print(ff)


#Q11
#Write a Python program to generate all permutations of a list in Python.

import itertools
print(list(itertools.permutations([1,2,3])))

#Q12
#Write a Python program to get the difference between the two lists.

a= [1, 3, 5, 7, 9]
l=[1, 2, 4, 6, 7, 8]
q = list(set(a) - set(l))
w = list(set(l) - set(a))
total_diff = q + w
print(total_diff)

#Q13
#. Write a Python program to append a list to the second list.

a = [1,2,3,4,5]
a1 = ['red','blue','green','white','red']
c = a+a1
print(c)

#Q15
#Write a Python program to find common items from two lists.
def comm(a,b):
    a_set = set(a)
    b_set = set(b)
    if(a_set & b_set):
        print(a_set & b_set)
    else:
        print("no common")


a = [1,2,3,4,5,6]
b = [5,7,8,9,10,11]
comm(a,b)


#Q16
#. Write a Python program to split a list based on first character of word.
from itertools import groupby
from operator import itemgetter

dd = ["ashish","ashu","suraj","rohit","raju","do","def","cat"]
for letter, words in groupby(sorted(dd),key=itemgetter(0)): 
    print(letter)
    for word in words:
       print(word)

#Q17
#Write a Python program to remove duplicates from a list of lists.
#Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#New List : [[10, 20], [30, 56, 25], [33], [40]]

import itertools
cc=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
cc.sort()
new = list(cc for cc,_ in itertools.groupby(cc) )
print(new)







