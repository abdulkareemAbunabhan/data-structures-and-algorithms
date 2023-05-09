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
        if(self.front_stack.top):
            if(self.back_stack.top):
                self.back_stack.push(node)
            else:    
             node.next=self.front_stack.top
             self.back_stack.top=node
        else:
            self.front_stack.top=node
        return self.__str__()    

    def dequeue(self):
        if(self.front_stack.top):
            if(self.back_stack.top):
                current=self.back_stack.top
                target=self.front_stack.pop()
                while(current.next != self.front_stack.top):
                    current=current.next
                current.next=None    
                self.front_stack.top=current
            else:
                target=self.front_stack.pop()
            return target       
        else:
            return "Empty queue"
        
    def __str__(self):
        output=""

        if self.front_stack == None:
            output="Empty Queue"
        else:
            if(self.back_stack.top):
                current=self.back_stack.top
                while(current.next != self.front_stack.top):
                    output+=f'{current.value} --> '
                    current=current.next
                output+=f'{current.value} --> {self.front_stack.top.value} -->'
            else:
                output+=f'{self.front_stack.top.value} --> '
            output+=" None"
        return(output)    