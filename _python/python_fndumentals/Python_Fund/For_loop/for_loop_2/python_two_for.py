   #####################
#### For loop Basic II ####
  ###### Ali Yahya ######
        ###########
##1-Biggie size :

list_biggie = [-1 ,2,3,4-22,44,55,11,-1]
for i in range(len(list_biggie)):
  if list_biggie[i] >= 0 :
   list_biggie[i] = "biggie"
   


##2-Count Positives:
list_count = [1,2,3,11,22,-20]
count = 0
for i in range(len(list_count)):
  if list_count[i] > 0 :
    count += 1
list_count.pop()
list_count.append(count)


#3-Sum Total:
list_sum = [1,2,3,4,10]

def sum_list(list_sum):
  sum = 0
  for i in range(len(list_sum)):
    sum +=list_sum[i]
  return sum

# 4- Average :

list_avarage = [10 , 4 ,3 , 44, 10]

def avarage_list(list_avarage):
  sum = 0
  for i in range(len(list_avarage)):
    sum += list_avarage[i]
  return sum / len(list_avarage)

# 5- Length

list_length =[1,2,3,4,5]

def length_lest(list_length):
  length = 0

  for i in range(len(list_length)):
    length +=1
  return length 

# 6- Minimum

list_minimum = [1,2,3,45,6,-33]

def minimum_list(list_minimum):
  min = list_minimum[0]
  for i in range(len(list_minimum)):
    if list_minimum[i] < min:
      min = list_minimum[i]
  return min

# 7- Maximum
maxmum_list =[22,33,12,120,300,12]

def maximum_list(list_maximum):
  max = list_maximum[0]
  for i in range(len(list_maximum)):
    if list_maximum[i] > max:
      max = list_maximum[i]
  return max

# 8-Ultimate Analysi: 
list_analaysis= [2,3,4,55 , -10, 20,-90]

def ultimate_analysis(list):
  return {"sumtotal":sum_list(list), "avarage":avarage_list(list) , "length":length_lest(list) , "min":minimum_list(list) ,"max": maximum_list(list)}

# 9-Reverse List :
list_rev = [1,2,3,4,5,6,7,8,9]

list_rev.reverse()


################################################################
print (list_biggie)
print(list_count)
print(sum_list(list_sum))
print(avarage_list(list_avarage))
print(length_lest(list_length))
print(minimum_list(list_minimum ))
print(maximum_list(maxmum_list))
print(ultimate_analysis(list_analaysis))
print(list_rev)