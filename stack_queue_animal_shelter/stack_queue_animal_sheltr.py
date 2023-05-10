from Node import Node
from Queue import Queue
class AnimalShelter:

    def __init__(self):
        self.shelter=Queue()

    def enqueue(self,animal):
        self.shelter.enqueue(animal)
        return self.shelter.__str__()
    
    def dequeue(self,pref="empty"):
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
            if(current==self.shelter.back):
                self.shelter.back=prev
            prev.next=current.next
            return current
        else:
            return self.shelter.dequeue()

