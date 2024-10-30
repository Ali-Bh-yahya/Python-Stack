# #1 this function will return 5
# def a():
#     return 5
# print(a())

# #2 tis function will return 10 becouse we added the two functions
# def b():
#     return 5
# print(b()+b())

# #3 this function will return 5 becouse its take first resturn in the function when it arrive in first resturn its will leave the function
# def c():
#     return 5
#     return 10
# print(c())

# #4 this function will return 5 its the same reason in 3

# def d():
#     return 5
#     print(10)
# print(d())

# #5 this function will print 5
# def e():
#     print(5)
# x = e()
# print(x)

#6 this function will print 3 , 5 and in the last none  becouse when i want print function i should use return function
# def f(b,c):
#     print (b+c)

# print(f(1,2) + f(2,3))

#7 this function will print 25 becouse they use str in function
# def g(a,d):
#     return str(a) + str(d)
# print(g(2,5))

#8 this function will prit (b=100) and return 10 

# def h(b):
#     b=100
#     print(b)
#     if b < 10 :
#       return 5
#     else : return 10

#     return 7

# print(h(100)  )

#9 in the first print for function its will return 7 in the second print  will return 14 in the third print will return 21
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# #10 this functin should return 8
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

#11 the out put in this code will be 500 ,500 , 300 and in the last 500 

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

#12 the out put in this code will be 500 ,500 , 300 and in the last 500 its the same 11 return in this example dont useful because i don't print function

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

#13 the out put in this code will be 500 ,500 , 300 and in the last 300 becouse we give the value of function to (b)  
# b = 500
# print(b)#500
# def a():
#     b = 300
#     print(b)#300
#     return b
# print(b)#500
# b=a()
# print(b)#300

#14  the out put in this code will be 1 ,3 and 2 
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

#15 
def a():
    print(1)#1
    x = b()
    print(x)#5
    return 10
def b():
    print(3)#3
    return 5
y = a()
print(y)#10