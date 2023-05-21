from node import Node

class Binary_trees:
    def __init__(self):
        self.root=None
        self.res = []
        self.temp=None

    def add(self,value):
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
                self.add(value)    
        
    def pre_order(self,arg=None,resu=None):
        if(resu is None):
            resu=[]
        if (arg==None):
            arg=self.root
            self.pre_order(arg,resu)
            return resu
        if(arg):
            resu.append(arg.value)
            if(arg.left):
               self.pre_order(arg.left,resu)
            if(arg.right):
                self.pre_order(arg.right,resu)

    def in_order(self,arg=None,resu=None):
        if(resu is None):
            resu = []
        if(arg==None):
            arg=self.root
        if(arg):
            if(arg.left):
                self.in_order(arg.left,resu)
            resu.append(arg.value)
            if(arg.right):
                self.in_order(arg.right,resu)
        if(arg == self.root):
            return resu
    
    def post_order(self,arg=None,resu=None):
        if(arg is None):
            arg = self.root
        if(resu is None):
            resu = []
        if(arg):
            if(arg.left):
                self.post_order(arg.left,resu)
            if(arg.right):
                self.post_order(arg.right,resu)
            resu.append(arg.value)
        if(arg is self.root):
            return resu

class Binary_search_tree(Binary_trees):
    def __init__(self):
        super().__init__()

    def adds(self,value,temp=None):
        node=Node(value)
        if(not self.root):
            self.root=node
            return
        if(temp==None):
            temp=self.root
        if(value>temp.value):
            if(temp.right):
                self.adds(value,temp.right)
            else:
                temp.right=node
                return
        elif(value<temp.value):
            if(temp.left):
                self.adds(value,temp.left)
            else:
                temp.left=node
                return
        else:
            return

    def contains(self,value,temp=None):
        if(not self.root):
            return "empty tree"
        if(temp == None):
            temp = self.root
        if(temp.value==value):
            return True
        elif(temp.value<value):
            if(temp.left):
             self.contains(value,temp.left)
            else:
                return False
        else:
            if(temp.right):
             self.contains(value,temp.right)
            else:
                return False
        return False
    
    def pre_order(self, arg=None, resu=None):
        return super().pre_order(arg, resu)
    
    def in_order(self, arg=None, resu=None):
        return super().in_order(arg, resu)
    
    def post_order(self, arg=None, resu=None):
        return super().post_order(arg, resu)