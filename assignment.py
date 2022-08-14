#Basic python

#Q1
# Write a Python program which accepts the user's first and last name and prints them in
#reverse order with a space between them.

name = ["Ashish","Hemant","Brahmadande"]
print(name[0][::-1],name[2][::-1])

#Q2
#Write a Python program which accepts a sequence of comma-separated numbers from the
#user and generates a list and a tuple with those numbers.
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')


list = ['3',' 5',' 7',' 23']
print(list)
tu = tuple(list)
print(tu)

#Q3
#Write a Python program to display the first and last colours from the following list.
#color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[3])



#Q5
#Write a Python program to print the calendar of a given month and year.
#Note : Use 'calendar' module.

import calendar
from re import A

x =int(input("enter the year:"))
y =int(input("enter the month:"))

print(calendar.month(x,y))


#Q10

#Write a Python program to print out a set containing all the colors from color_list_1 which are
#not present in color_list_2.
#Test Data :
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#Expected Output :
#{'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))
#print(color_list_2.difference(color_list_1))


#18
#Write a Python program to get an absolute file path.
from pathlib import Path
fpath = Path('assignment.py').absolute()
print(fpath)

#Q28
#Write a Python program to clear the screen or terminal.

import os
os.system('cls')

