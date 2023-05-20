from node import Node

class Binary_trees:
    def __init__(self):
        self.root=None
        self.res = []
        self.temp=None

    def add_leef(self,value):
        node=Node(value)
        if(not self.root):
            self.root=node
            self.temp=self.root
            return self.res.append(value)
        else:
            if(not self.temp.left):
                self.temp.left=node
                return self.res.append(value)
            if(not self.temp.right):
                self.temp.right=node
                return self.res.append(value)
            else:
                self.temp=self.temp.left
                self.add_leef(value)    
        
    def pre_order(self,arg=None,resu=[]):
        if (arg==None):
            arg=self.root
            self.pre_order(arg)
            return resu
        if(arg):
            resu.append(arg.value)
            if(arg.left):
               self.pre_order(arg.left)
            if(arg.right):
                self.pre_order(arg.right)

    def in_order(self,arg=None,resu=[]):
        if(arg==None):
            arg=self.root
        if(arg):
            if(arg.left):
                self.pre_order(arg.left,resu)
            resu.append(arg.value)
            if(arg.right):
                self.pre_order(arg.right,resu)
        if(arg == self.root):
            return resu