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
          
    def insert_before(self, value, newValue):
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
    def linked_list_fromEnd(self,k):
       if (self.head is None):
          return "Failed"
       else:
         counter = 1
         current = self.head
         while(k != counter):
            current = current.next
            counter+=1
         return current.value  

    #Challenge 8 LinkedList Zip:    
    def zipLists(list1, list2):
        current1 = list1.head
        current2 = list2.head
        nList=Linked_list()
        while True:
            if current1 :
                nList.append(current1.value)
                current1=current1.next
            if current2:
                nList.append(current2.value)
                current2=current2.next

            if not current1 and not current2:
                break

        return nList             
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