class Node:
    def __init__(self, data):
      self.data =data
      self.next = None
    
new_node = Node(1)
head =new_node
node=Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)

new_node.next = node
node.next = node2
node2.next =node3
node3.next = node4
node4.next = node5

currunt = head


while currunt is not None:
  print(currunt.data)
  currunt= currunt.next


#delete the first node :
temp = head.next
head.next = None
head = temp
print(head.data)

print("\n")

#delete the tail node:
currunt_tail = head

while currunt_tail.next.next is not None:
    currunt_tail = currunt_tail.next
currunt_tail.next = None
cheack = head
while cheack is not None:
  print(cheack.data)
  cheack = cheack.next

#delete the middile node:

position = 3

middle =head

for i in range(1, position-1):
   middle = middle.next
middle = middle.next.next



