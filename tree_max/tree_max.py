from node import Node

class Binary_trees:
    def __init__(self):
        self.root=None
        self.max=None

    def adds(self,value,temp=None):
        """this method adds nodes to binary tree randomly"""
        node=Node(value)
        if(self.max is None or value > self.max):
            self.max=value    
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
        """this method used to traverse on the tree by ordering the root first then the left leaf then the right"""
        if(self.root is None):
            return []
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
        """this method used to traverse on the tree by ordering the left leaf first then the root then the right"""
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
        """this method used to traverse on the tree by ordering the left leaf first then the right leaf then the root"""
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
    def tree_max(self):
        """this method used to traverse on a tree and return the maxmum value in it"""
        def reusable_traverse(temp=self.root,max=None):
            if(temp):
                if(max is None or max < temp.value):
                 max=temp.value
                if(temp.left):
                 max=reusable_traverse(temp.left,max)
                if(temp.right):
                 max=reusable_traverse(temp.right,max)
                return max
            else:
                return "empty tree"       
        return reusable_traverse()