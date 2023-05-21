from node import Node

class Binary_trees:
    def __init__(self):
        self.root=None

    def adds(self,value,temp=None):
        node=Node(value)
        if(not self.root):
            self.root=node
            return
        if(temp is None):
            temp=self.root
        if(temp):
            if(not temp.left):
                temp.left=node
                return
            if(not temp.right):
                temp.right=node
                return
            else:
                temp=temp.left
                self.adds(value,temp)    
        
    def pre_order(self,arg=None,resu=None):
        if(self.root is None):
            return "empty tree"
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

    def add(self,value,temp=None):
        node=Node(value)
        if(not self.root):
            self.root=node
            return
        if(temp==None):
            temp=self.root
        if(value>temp.value):
            if(temp.right):
                return self.add(value,temp.right)
            else:
                temp.right=node
                return
        elif(value<temp.value):
            if(temp.left):
                return self.add(value,temp.left)
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
        elif(value<temp.value):
            if(temp.left):
             return self.contains(value,temp.left)
            else:
                return False
        else:
            if(temp.right):
             return self.contains(value,temp.right)
            else:
                return False
        return False
    
    def pre_order(self, arg=None, resu=None):
        return super().pre_order(arg, resu)
    
    def in_order(self, arg=None, resu=None):
        return super().in_order(arg, resu)
    
    def post_order(self, arg=None, resu=None):
        return super().post_order(arg, resu)