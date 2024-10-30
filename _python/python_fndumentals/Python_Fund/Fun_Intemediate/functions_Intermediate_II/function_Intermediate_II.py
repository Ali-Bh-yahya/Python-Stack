#1.Update Values in Dictionaries and Lists

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
#1_Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]:
x[1][0] = 15
print(x)
#2_Change the last_name of the first student from 'Jordan' to 'Bryant':

students[1]["first_name"] = "Brynt"

print(students)

#3_In the sports_directory, change 'Messi' to 'Andres':
sports_directory["soccer"][0] = "Andres"
print (sports_directory)

#4_Change the value 20 in z to 30:

z[0]["y"]= 30

print(z)

#2.Iterate Through a List of Dictionaries

students = [
      {'first_name':  'Michael', 'last_name' : 'Jordan'},
      {'first_name' : 'John', 'last_name' : 'Rosales'},
      {'first_name' : 'David', 'last_name' : 'Beckham'}
 ]
def iteratedictionary(student):
  for student in students:
    print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")



iteratedictionary(students) 

#3.Get Values From a List of Dictionaries

def iterateDictionary(key_name,students):
  for student in students:
    print(f"{student[key_name]}")
  
iterateDictionary('first_name', students)
#4-Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for key , value in some_dict.items():
    print(f"{len(value)} {key.upper()}")
    for elemeant in value:
        print(elemeant)
    print("\n")
printInfo(dojo)
