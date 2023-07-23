import math
####################### Linked List setup ################################        
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
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
################################### hashmap setup #######################    
class HashTable():
    def __init__(self,size=7):
        self.size =size
        self.map = [None]*size

    def CustomHash(self,key):
       """this method takes the key and return an index that suits the key provided depending on the algorithim"""
       total=0
       key=str(key)
       if len(key)>1:
            total+=ord(key[1])
       if len(key)>3:
           total+=ord(key[3])
       if len(key) > 5:
           total+=ord(key[5])
       total+=len(key)    
       total=int(math.log10(total))
       return total%7
    
    def Set(self,key,value):
        """this method used to set the key and value to the array and handels the collesions"""
        hashed_key=self.CustomHash(key)
        if self.map[hashed_key] is None:
            self.map[hashed_key]=[key,value]
        elif isinstance(self.map[hashed_key],Linked_list):
            self.map[hashed_key].append([key,value])
        else:
            chain=Linked_list()
            chain.append(self.map[hashed_key])
            chain.append([key,value])
            self.map[hashed_key]=chain

    def HasKey(self,key):
        """this method used to check if a provided key is in the table or not"""
        hashed_index=self.CustomHash(key)
        if self.map[hashed_index] is None :
            return False
        elif isinstance(self.map[hashed_index],Linked_list):
            current=self.map[hashed_index].head
            while current:
                if current.value[0] == key :
                    return True
                current=current.next
            return False
        return True    

    def GetKeyValue(self,key):
        """this method used to get a value related to a key"""
        hashed_index=self.CustomHash(key)
        if self.map[hashed_index] is None :
            return "Not exist"
        elif isinstance(self.map[hashed_index],Linked_list):
            current=self.map[hashed_index].head
            while current:
                if current.value[0] is key :
                    return f'the value of {key} is {current.value[1]}'
                current=current.next
            return "Not exist"
        return self.map[hashed_index][1]
    
    def AllKeys(self):
        """this method responsible of returning all the keys related to the hashTable"""
        keys_list=[]
        for i in self.map:
            if i is None:
                pass
            elif isinstance(i,Linked_list):
                current=i.head
                while current:
                    keys_list.append(current.value[0])
                    current=current.next
            else:
                keys_list.append(i[0])
        return keys_list