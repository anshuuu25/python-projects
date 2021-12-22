class Node:


   def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null


class LinkedList:


   def __init__(self):
       self.head = None

def show(nameofll):
    node = nameofll.head
    while node is not None:
          print (node.data)
          node=node.next
    
         
linkedlist1 = LinkedList()

firstnode = Node('1')
linkedlist1.head = firstnode
firstnode.next = Node('2')
firstnode.next.next = Node('3')
show(linkedlist1)
