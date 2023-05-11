from stack_queue_animal_sheltr import AnimalShelter
from Node import Node

shelter=AnimalShelter()
meow=Node("catty","cat")
woah=Node("danger","dog")
shelter.enqueue(woah)
print(shelter.enqueue(meow))

print(shelter.dequeue())
print(shelter.enqueue(woah))
print(shelter.shelter.__str__())
print(shelter.dequeue("dog"))
print(shelter.shelter.__str__())
