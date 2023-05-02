from node import Node
class Linked_list:
    def __init__(self):
        self.head=None

    def insert(self,value):
      """this method used to insert a method at the beguning of linked list"""
      node = Node(value)             
      node.next=self.head
      self.head=node
      
    def includes(self,value):
        """this method used to check if there the value given is included in the linked
        nods or not"""
        current=self.head
        while(current != None):
         if(current.value==value):
            return True
         current=current.next

        return False
    
    def append(self,value):
       """this method used to add a node at the end of a linked list"""
       node=Node(value)
       if(self.head == None):
          self.head=node
       else:
          current=self.head
          while(current.next):
             current=current.next   
          current.next=node
          
    def insert_before(self, value, newValue):
     """this method used to add a node before specefic node in the linked list"""
     node = Node(newValue)
     if self.head is None:
        self.head = node
        return

     if self.head.value == value:
        node.next = self.head
        self.head = node
        return

     current = self.head
     while current.next is not None:
        if current.next.value == value:
            node.next = current.next
            current.next = node
            return
        current = current.next
     raise ValueError(f"{value} not found in linked list")
         
    def insert_after(self,value,newValue):
       """this method used to add a node after specefic node in the linked list"""
       node = Node(newValue)
       if(value is None):
          self.append(node)    
          return
       current =self.head
       while(current.value is not value):
          current=current.next
       if(current.next is None):
          current.next=node
       else:
          prev=current        
          node.next=current.next
          prev.next=node
    def delete_node(self,value):
       if(self.includes(value)):
         current=self.head
         if(current.value is value):
            self.head=current.next
            return
         while(current.next.value is not value):
            current=current.next
         prev=current
         current=current.next
         prev.next=current.next
       else:
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