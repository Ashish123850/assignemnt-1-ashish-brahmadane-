#Q1
#Write a Python program to calculate the length of a string.

st = "ashwamedham"
print(len(st))

#Q2
#Write a Python program to count the number of characters (character frequency) in a string.
strs ="ashwamedham"

dict ={}
for i in strs:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1
print("the output " + str(dict))


#Q3
# Write a Python program to get a string from a given string where all occurrences of its
#first char have been changed to '$', except the first char itself.
str = "restart"
modified_str = ''
for char in range(0, len(str)):
    if(str[char] == 'a'):
        modified_str += '$'
    else:
        modified_str += str[char]
 
print(modified_str)

#Q5.
#  Write a Python function that takes a list of words and returns the length of the longest one.
a =["Ashish","mites","nehu"]
longest = max(a, key=len)
print(longest)




#Q6.
#  Write a Python script that takes input from the user and displays that input back in
#upper and lower cases.

d =input("enter the data:")
print(d.upper())
print(d.lower())

#Q7
#Write a Python program that accepts a comma separated sequence of words as input
#and prints the unique words in sorted form (alphanumerically).

nn = input("enter the words")
wo = [words for words in nn.split(",")]
print(",".join(sorted(list(set(wo)))))


#Q8
#Write a Python program to get the last part of a string before a specified character.
ss = 'https://www.w3resource.com/python-exercises/string'
print(ss.rsplit('-', 1)[0])

#9
#Write a Python program to display formatted text (width=50) as output.

import textwrap
a ="Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed."
print(textwrap.fill(a,width=50)) 


#Q10
#Write a Python program to count occurrences of a substring in a string.

a = "Kokan is the beauty of the nature beauty is like as swarg"
print(a)
print(a.count("beauty"))

#Q11
# Write a Python program to reverse a string
str = "ashwamedham"
print(str[::-1])

#Q12
# Write a Python program to lowercase first n characters in a string.

stt ="ASHWAMEDHAM"
print(stt.lower())