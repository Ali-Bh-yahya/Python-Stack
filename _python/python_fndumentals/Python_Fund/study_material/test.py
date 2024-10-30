my_list = []

#declare  and add iteams to an array in Pathon

my_list.append(22)
my_list.append(33)
my_list.append(44)
my_list.append(55)

print(my_list)

# Remove the iteam in arrry

my_list.remove(55)

print(my_list)

# Remove the last iteam in arrry
my_list.pop()

print(my_list)

#Concatenating Strings and Vaariables with the print function

name = "Zeneerrttds"

print(name)

print("my name is " + name )
#for loop with add iteams in the list
first_list = []

for i in range(10):
 first_list.append("ali")
 print(first_list[i])

#concatenate a string with the integer part:
my_name = "mohammad"
my_age = 20

#print("The number is " + my_number)this is not correct

print("The number is " + str(my_age))

#1-f-strings (formatted string literals):

print(f"{my_age} and {my_name}")

#2-format metheod :

message = "{} and {}".format(my_name,my_age)

print(message)

#4-Old style string formatting(%):

message_2 = "%d and %s" % (my_age,my_name)

print(message_2)

#The following is a list of commonly used  sring methode:
#string.upper()
uper_name = name.upper()
print(uper_name )
#string.lower()
lower_name=uper_name .lower()
print(lower_name)
#string.count(substring)
print(lower_name.count("e"))
#string.isalnum()
name_2 = "python 2"
name_3 ="python2"
name_4 = "python2"
print(name_2.isalnum()) 

print(name_4.isalnum())

print(name_3.isalnum())

#Pass: python , if we write a function or class empty we will have syntax error to solve this problem we write a Pass
#example: 
def function_empty():
   pass

function_empty()

# Parameters and Arguments
