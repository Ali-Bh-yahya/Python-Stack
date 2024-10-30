
class Node:
    def __init__(self, data):
      self.data =data
      self.next = None
    
new_node = Node(400)
head =new_node
node=Node("Ali")
node2 = Node("Bahaa")
node3 = Node("Yahya")

new_node.next = node
node.next = node2
node2.next =node3


count = 0
currunt = head


while currunt is not None:
  print(currunt.data)
  currunt= currunt.next
  count += 1
print(f"count of nodes = {count}")

count = 0
currunt = head
# while currunt is not None and count < 2:
#   print(currunt.data)
#   currunt= currunt.next
#   count += 1
# # print(currunt.data)
# print(f"count of nodes = {count}")
# for i in range( 1,3 ,1):
#   print(currunt.data)
#   currunt= currunt.next
# for i in range( 1,2 ,1):
#   print(currunt.data)
#   currunt = currunt.next
print("\n")
tail_node = Node("400$")

node3.next = tail_node
tail_node.next = None
nod = new_node
while nod is not None:
  print(nod.data)
  nod = nod.next
  print("\n Example 3:")

middle_node = Node("Bod_cam")##postition 3

node2.next = middle_node
middle_node.next = node3
count = 0
while currunt is not None:
   currunt = currunt.next
   count += 1 
currunt = head
for i in range(1,count):
   print(currunt.data)
   currunt = currunt.next

print("\n Example 4:")
postition = 4
node_after_middle = Node("after middle")
currunt = head
for i in range(1,postition-1):
   currunt = currunt.next

node_after_middle.next = currunt.next
currunt.next = node_after_middle
  
count = 0
while currunt is not None:
   currunt = currunt.next
   count += 1 

print("ttttttt",count)
currunt2 = head
for i in range(0,count):
   print("test",currunt2.data)
   currunt2 = currunt2.next





  
