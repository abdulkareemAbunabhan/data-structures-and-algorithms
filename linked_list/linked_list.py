from node import Node
class Linked_list:
    def __init__(self):
        self.head=None

    def insert(self,value):
      node = Node(value)             
      node.next=self.head
      self.head=node
    def includes(self,value):
        current=self.head
        while(current != None):
         if(current.value==value):
            return True
         current=current.next

        return False
                  
    def __str__(self):
        output=""

        if self.head == None:
            output="Empty Linked List"
        else:
            current=self.head
            while(current):
                output+=f'{current.value} --> '
                current=current.next
            output+=" None"
        return(output)                