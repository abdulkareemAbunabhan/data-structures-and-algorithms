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
        if(self.shelter.front.value["species"] == pref):
            res={"name":self.shelter.front.value["species"],
                 "species":self.shelter.front.value["species"]}
            self.shelter.dequeue()
            return res
        current= self.shelter.front
        prev=current
        while(current is not None and current.value["species"] != pref):
            prev=current
            current=current.next
        if(current):
            if(current==self.shelter.rear):
                self.shelter.rear=prev
            prev.next=current.next
            obj={"name":current.value["name"],"species":current.value["species"]}
            return obj
        else:
            """this line is for the stech goal"""
            return self.shelter.dequeue()

