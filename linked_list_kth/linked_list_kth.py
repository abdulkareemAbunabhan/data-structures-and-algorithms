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
       """this method deletes the node that match the given value if there is no match will return false"""
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
    
    def linked_list_fromEnd(self,k):
       """this method return the value of the kth node from the end"""
       if(k==0):
          return None
       if (self.head is None):
          return "Empty"
       else:
         counter = 0
         current = self.head
         while(current):
            current = current.next
            counter+=1
         if(k>counter):
            return "Linked list is shorter than u think"   
         target= counter - k 
         counter =0
         current= self.head
         while(counter != target):
            current=current.next
            counter+=1   
         return current.value 
  
    def reverser(self):
       current=self.head
       prev=self.head
       nett = current.next
       while(current.next):
          current=nett
          nett=current.next
          if (prev==self.head):
             prev.next=None
          current.next = prev
          prev = current
       self.head=current   
       return self.__str__()
    def isPalindrome(self):
       if(not self.head):
          return "Empty linked list"
       current=self.head
       reversed=Linked_list()
       while(current):
          reversed.insert(current.value)
          current=current.next
       if(self.__str__() == reversed.__str__()):
          return True
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