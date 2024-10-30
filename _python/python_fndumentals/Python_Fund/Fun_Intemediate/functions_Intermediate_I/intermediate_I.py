import random
#1- returns a random floating number between 0.000 and 1.000
# list= [22.00,0.00,30.00,45.5,80.7,100.4]
def random_numbers(list):
  # num =list.random()not a method of the list itself.
  # num = random.choice(list) this a random its true fo the list
  num = random.random()
  return num

print (random_numbers(list))
#2- returns a random floating number between 0.000 and 50.000
def random_numbers_half():
  # num = random.uniform(0 ,50) 
  num = random.random() * 50
  return num

print(random_numbers_half())

#3-  returns a random floating number between 10.000 and 35.000

def random_numbers_range():
  num = random.random() * 25 + 10
  return num

print(random_numbers_range())

#4-  returns the rounded integer value of num

def random_numbers_integer():
  num = random.random()*10 + 4
  print(num)
  num =round(num) # round functtion its to convert from float to int
  return num
print(random_numbers_integer())
