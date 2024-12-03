sum = 0
product = 1
lists = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(lists.length):
  sum += lists[i]

for j in range(lists.length - 1):
  product *= lists[j]

  print("Sum: ", sum)
  print("Product: ", product)