import math
from linked_list import Linked_list
class HashTable():
    def __init__(self,size=7):
        self.size =size
        self.map = [None]*size

    def CustomHash(self,key):
       """this method takes the key and return an index that suits the key provided depending on the algorithim"""
       total=0
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
                if current.value[0] is key :
                    return True
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
        return f'the value of {key} is {self.map[hashed_index][1]}'
    
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