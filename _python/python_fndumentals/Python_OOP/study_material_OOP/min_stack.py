class Node :
  def __init__(self,data):
    self.data = data
    self.min = data
    self.next =None

class Min_stak:
  def __init__(self):
    self.top = None
    
  def push(self, data):
    new_node = Node(data)
    if self.top is not None :
      new_node.min = min(new_node.min,self.top.min)
      new_node.next =self.top
      self.top = new_node
    else :
      self.top =new_node

  def pop(self):
    if self.top is None:
      return None
    else:
      temp_data = self.top
      self.top = self.top.next
      del temp_data
  def peek(self):
    if self.top is None:
      return None
    else:
      return self.top.data
    
  def get_min(self):
    if self.top is None:
      return None
    else:
      return self.top.min
    
ex_1 = Min_stak()

ex_1.push(4)
print(ex_1.get_min())
ex_1.push(100)
print(ex_1.get_min())
ex_1.push(20)

print(ex_1.get_min())

