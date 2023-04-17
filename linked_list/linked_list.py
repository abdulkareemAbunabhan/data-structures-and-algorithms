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
    
    def append(self,value):
       node=Node(value)
       if(self.head == None):
          self.head=node
       else:
          current=self.head
          while(current.next):
           current=current.next   
          current.next=node
          
    def insert_before(self,value,newValue):
       node=Node(newValue)
       current=self.head
       if(value==current):
          node.next=current.next
          current.next=node
       else:
         while(current.next):
             if(current.next.value==value):
                node.next=current.next
                current.next = node
                break
             current=current.next
         
        
          
                  
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