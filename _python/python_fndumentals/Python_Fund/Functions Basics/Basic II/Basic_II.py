#1 Countdown 
def count_down(number):
   number_list = []
   for num in range(number ,0 , -1):
      number_list.append(num)
   return number_list

print(count_down(5))

#2 Print and Return
def print_return(a,b):
 
  for i in range(2):
     if i == 0:
      print(a)
     else :
       return b
  return None 
    
      
print(print_return(1,2)) 

#3 First Plus Length
# we need print the result of the addition the first ilement of the list withe the length
arr_list = [1, 2, 3, 4, 5]

def first_plus_length(arr):
  length = len(arr)
  print(arr[0]+length)
  

first_plus_length(arr_list)

#4 Values Greater than Second
def values_greater_than_second(arr):
 second_arr = []
 if len(arr) > 2:
  for i in range(len(arr)-1):
      if arr[i] > arr[1]:
        second_arr.append(arr[i])

 return second_arr
 
print (values_greater_than_second([2,1,4,5,2,1,33,42,1]))
#This Length, That Value 

def length_that_value(a,b):
  list_value = []
  for i in range(a):
    list_value.append(b)
  return list_value

print(length_that_value(30,5))
  


 
