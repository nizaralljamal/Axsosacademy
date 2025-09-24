#----------------------------------------------
x = [ [5,2,3], [10,8,9] ] #
#----------------------------------------------
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},# {}
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#----------------------------------------------
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
#----------------------------------------------
z = [ {'x': 10, 'y': 20} ] 
#----------------------------------------------


#q1.
#change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#q2.
#change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

#q3.
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#q4.
#Change the value 20 in z to 30
z[0]['y'] = 30
print(z)



students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(0,len(students)):
        print(students[i])

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key, list):
    for i in range(0,len(list)):
        print(list[i][key])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    print(str(len(dict['locations'])) +" LOCATIONS")
    for i in range(0,len(dict['locations'])):
        print(dict['locations'][i])
    print()
    Instructors = dict['instructors']
    print(str(len(Instructors)) +" INSTRUCTORS")
    for i in range(0,len(Instructors)):
        print(Instructors[i])


printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon










