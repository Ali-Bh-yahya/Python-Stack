#the traditional way to swap two 
# variables in array is 3 lines
# this way we was use in javascript
#example:
# list_array =[1,2,3,4,5]

# temp = list_array[1]
# list_array[1] = list_array[0]
# list_array[0] =temp

# print(list_array)

# in python we can swap in one line
#easier than in javascript

# arr = [1,2,3,4,5]
# arr[0] , arr[1] =  arr[1] , arr[0]
# arr[2] , arr[3] = arr[3] , arr[2]
# print(arr)

#Bubble Sort exercise with it [6,5,3,1,8,7,2,4]
#1 will make a function call bubble_sort
def bubble_sort(list_a):
  length = len(list_a) -1
  #print(length) to check length
  boolean =False
  while not boolean:
    boolean =True
    for i in range(0,length,1):#0->1 -> 2 
      if list_a[i] > list_a[i+1]: #6 > 5  : 6>3 : 6>1 :
        # list_a[i] , list_a[i+1] = list_a[i+1], list_a[i]
        swap = list_a[i]
        list_a[i] = list_a[i+1]
        list_a[i+1] = swap
        boolean = False
  return list_a
print(bubble_sort([6,5,3,1,8,7,2,4])) #-> [5,3,1,6,7,2,4,8]

#know we will talk about Ternary Operator
#in python
#its like <result_if_true>if <condition> else <result_if_false>
#in the traditional way use if statement
# stack = 2

# if stack >= 2:
#   print("the stack equal 2 or greater than it")
# else:
#   print("good bye!")

#ternary operator
# a = 20
# print("Hi in ternary operator!" if a == 30 else " good bye!")

#now i use the lambdas function it is anonymous function
# they are handy we only need to use the function once
#they are lightweight when we break down complex tasks into small,specific once
# they are convenient as arguments to function that require function as parameters

#i defined the square () function that takes in one parameter (num)

# def square(num):
#   x = num **2
#   return x
# print(square(2))

#in lambda function we write for  one variable:
# x = 33
# print((lambda x: x**2)(x))

# in lambda function we write for list of varibals:

# list_nums = [2,3,4,5,6]
# print(list(map(lambda x: x**2, list_nums)))
