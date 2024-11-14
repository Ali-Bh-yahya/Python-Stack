def factoriall(n):
  result = 0
  if n >=1:
    print(n)
    return int(n * factoriall(n-1))
  else:
    return 1
  
print(factoriall(5))

def fact(n):
  for i in range(n):
    n = n*i
  return n

print(fact(5))


  
