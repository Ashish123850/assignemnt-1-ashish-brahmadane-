

#Dictionary
#Q1
# Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)

#Q2
#Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

a= {0: 10, 1: 20}
a.update({2:30})
print(a)

#Q3
# Write a Python script to concatenate following dictionaries to create a new
#one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2,dic3) : dic4.update(d)
print(dic4)


#Q4
#Write a Python program to iterate over dictionaries using for loops
t = {'a': 'ashish', 'b': 'mitesh', 'c': 'mayur'}

for key, value in t.items():
    print(key, value)   