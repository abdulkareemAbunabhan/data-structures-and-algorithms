from Stack import Stack
from Node import Node

class max_stack:
    def __init__(self):
        self.stack=Stack()
        self.max_stack=Stack()

    def push(self,value):
        self.stack.push(value)
        if(self.max_stack.top == None or self.max_stack.top.value<value):
            self.max_stack.push(value)

    def pop(self):
        poped=self.stack.pop()
        if(poped == self.max_stack.peek):
            self.max_stack.pop()
        return poped

    def getMax(self):
        if(self.max_stack.top):
            return self.max_stack.peek()
        else:
            raise ValueError("Empty Stack")    