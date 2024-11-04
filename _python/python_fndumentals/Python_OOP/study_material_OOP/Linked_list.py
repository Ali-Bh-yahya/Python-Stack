class Node:
  def __init__(self , data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail =None
    self.length = None

    def append(self, data):
      new_node = Node(data)
      if self.head is None:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node
        self.tail = new_node
      self.length += 1

    def prepend(self, data):
      new_node = Node(data)
      if self.head is None:
        self.head = new_node
        self.tail = new_node
      else:
        new_node.next = self.head
        self.head = new_node
        self.length += 1
      def get_node(self,index):
        if index < 0 and index > self.length:
          return None
        current_node =  self.head
        for i in range (index):
          current_node = current_node.next 
        return current_node



    
