"""
Assignment: Functions Intermediate II
Objectives:
Practice writing functions and looping over dictionaries
Better understand how to traverse through an array of dictionaries or through a dictionary of arrays.
--------------------------
"""
"""
--------------------------
1. Given

x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
--------------------------
"""
# A) How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print("\nx = ", x)

# B) How would you change the last_name of the first student from 'Jordan' to "Bryant"?

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"] = "Bryant"
print("Student is now: ", students[0])

# C) For the sports_directory, how would you change 'Messi' to 'Andres'?

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
print("Soccer is now ", sports_directory["soccer"])

# D) For z, how would you change the value 20 to 30?

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print("20 changed to", z[0]['y'])

"""
2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
"""

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(students):
    for i in students:
        print(i)
iterateDictionary(students)

def iterateDictionary_2(students):
    for i in students:
        print("first_name:", i["first_name"]+", " "last_name:", i["last_name"],)
iterateDictionary_2(students)

"""
3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

Michael
John
Mark
KB
"""

def iterateDictionary_3(key, dict):
    for i in dict:
        print(i[key])

iterateDictionary_3('first_name', students)

"""
4.  Say that

Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output

7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank

8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def dojoInfo(dojo):
    print("\n")
    print(len(dojo["locations"]), "locations".upper())
    for x in range (len(dojo["locations"])):
        print(dojo["locations"][x])
    print("\n")
    print(len(dojo["instructors"]), "instructors".upper())
    for x in range (len(dojo["instructors"])):
        print(dojo["instructors"][x])
    print("\n")
dojoInfo(dojo)

# for student in students:
#     s = ""
#     for key in student:
#         s += key + " - " = student[key] + " "
#
#         # f string , questions
#
#         # .upper()
#
#         i2
#         jk
#         j7\
#         j%
#
#         # printing an empty string

def revString(ourString):
    newString = ""
    for i in range(len(ourString)-1, 0, -1):
        newString += ourString[i]
    return newString
print(revString('Hello World!'))
