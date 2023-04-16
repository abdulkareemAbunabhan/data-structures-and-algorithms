from node import Node
class Linked_list:
    def __init__(self):
        self.head=None

    def insert(self,value):
      node = Node("A") 
      if self.head is None:
           self.head=node
      else:
         current = self.head
         while current.next is not None:
             current=current.next
         current.next=node             

    def includes(self,key):
        current=self.head
        if(current is None):
            return "Not found"
        elif(current is not None):
            if(current == key):
                self.head=current.next
                current = None
                return  True 
        else:
            while(current is not Node):
                if current.value==key
                break
                    





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
        return output               