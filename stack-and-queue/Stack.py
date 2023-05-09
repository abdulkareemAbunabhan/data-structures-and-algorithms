from Node import Node 

class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,value):
        node=Node(value)
        if not self.top:
            self.top=node
            self.size+=1
        else:
            node.next=self.top
            self.top=node
            self.size+=1
        return self.__str__()

    def pop(self):
        if self.top:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            self.size-=1
            return temp.value
        else:
            raise ValueError("Empty stack")

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise ValueError("Empty stack")

    def isEmpty(self):
        return not self.size            
    
    def __str__(self):
        output=""

        if self.top == None:
            output="Empty stack"
        else:
            current=self.top
            while(current):
                output+=f'{current.value} --> '
                current=current.next
            output+=" None"
        return(output)