from Node import Node
from Queue import Queue
class AnimalShelter:

    def __init__(self):
        self.shelter=Queue()

    def enqueue(self,animal):
        """this method enqueue to the back of the queuea and takes a node got name and species attributes as an argument"""
        self.shelter.enqueue(animal)
        return self.shelter.__str__()
    
    def dequeue(self,pref="empty"):
        """this method is dequeue from the queue depending on pref value if no pref provided will dequeue from the 
        first node in the queue and will return object contains the name and the species of the animal"""
        if not self.shelter.front:
            return self.shelter.dequeue()
        if(self.shelter.front.species == pref):
            res={"name":self.shelter.front.name,
                 "species":self.shelter.front.species}
            self.shelter.dequeue()
            return res
        current= self.shelter.front
        prev=current
        while(current is not None and current.species != pref):
            prev=current
            current=current.next
        if(current):
            if(current==self.shelter.rear):
                self.shelter.back=prev
            prev.next=current.next
            obj={"name":current.name,"species":current.species}
            return obj
        else:
            """this line is for the stech goal"""
            return self.shelter.dequeue()

