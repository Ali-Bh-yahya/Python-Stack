class Stack:
  class Node:
    def __init__ (self , data):
      self.data = data
      self.next = None
  def __init__(self):
    self.head = None
    self.size = 0
  def len(self):
    return self.size
  def is_empty(self):
    return self.size == 0
  def push(self, data):
    self.head = self.Node(data,self.head)
    self.size += 1
  def pop(self):
      result =self.head.data
      self.head = self.head.next
      self.size -=1
      return result
  def top(self):
    return self.head.data
  
  s = Stack()
  
