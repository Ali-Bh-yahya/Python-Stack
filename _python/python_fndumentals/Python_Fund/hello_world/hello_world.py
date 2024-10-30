#Write the code to print a literal string saying "Hello World"
print("Hello World")

#Store my name in a variable , and then use it to print  the string "Helo {{Ali}}"

name = "Ali"
print("Helo",name)

#Store my favorite number in a variable , and then use to print the string "Helo"{{44}}

favorite_number = 44
print(f"Helo{favorite_number}")

# BOUNUS: I can solve it with  f-strings (formatted string literals):{print(f"{my_age} and {my_name}")} ,   add str_fun ,
#format metheod : {message = "{} and {}".format(my_name,my_age)} and Old style string formatting(%):{message_2 = "%d and %s" % (my_age,my_name)}

#Store 2 of my favorite foods in varibles , and then use them to print the string "I have to eat {{food_one}} and {{food_two}}"
#1-with the format method:

food_one = "pizza"
food_two = "pasta"
message = "I have to eat {} and {} .".format(food_one,food_two)
print(message)

#2- with the str.fstring method:

print(f"I have to eat {food_one} and {food_two} .")

