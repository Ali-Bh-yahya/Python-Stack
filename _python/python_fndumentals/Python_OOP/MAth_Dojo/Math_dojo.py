class Mathdojo:
  def __init__(self):
    self.result = 0
  def add(self, num, *nums):
    self.result += num
    for n in nums:
      self.result += n
    return self
  def substract(self,num,*nums):
    self.result -= num
    for n in nums:
      self.result  -= n
    return self

x = Mathdojo()
y = Mathdojo()
x.add(3).add(2,3).add(33).add(1).add(2,44)
y.substract(20).substract(33).substract(20)


print(x.result)
print(y.result)




def printZakInfo(*args):
  print(args)

