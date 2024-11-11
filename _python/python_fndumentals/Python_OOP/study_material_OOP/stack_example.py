class Node :
  def __init__(self ,  data ):
    self.data = data
    self.next = None

class stack :
  def __init__ (self):
    self.top = None
    # self.min_stack = None

  def is_empty (self):
    return self.top is None
  
  def push(self , data =None):
    new_node = Node(data)
    if  self.top is None:
      new_node.next = None
      self.top = new_node
    elif self.top is not None:
      new_node.next = self.top
      self.top = new_node
    
  def pop(self):
    if self.is_empty():
      return None
    else:
      temp =self.top
      self.top =self.top.next
      del temp

  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.top.data
    
  
first_stack = stack()

first_stack.push(5)
print(first_stack.peek())
first_stack.push(2)
print(first_stack.peek())
first_stack.push(3)
print(first_stack.peek())

first_stack.pop()

print(first_stack.peek())




