from Node import Node
from stack import Stack
class PseudoQueue:

    def __init__(self):
        front_stack=Stack()
        back_stack=Stack()
        self.front_stack=front_stack
        self.back_stack=back_stack

    def enqueue(self,value):
        node=Node(value)    
        queue=PseudoQueue()
        if(queue.front_stack.top):
            if(queue.back_stack.top):
                queue.back_stack.push(node)
            else:    
             node.next=queue.front_stack.top
             queue.back_stack.top=node
        else:
            queue.front_stack.push(node)

    def dequeue(self):
        queue=PseudoQueue()
        if(queue.front_stack.top):
            if(queue.back_stack.top):

            else:
                queue.front_stack.pop()    
        else:
            return "Empty queue"