

def power_recurison(x, n):
  if n == 0:
    return 1
  elif n <0:
    return 1 / x * power_recurison(x, n+1)
  else:
    return x * power_recurison(x,n-1) 


print(power_recurison(0.00001,4))