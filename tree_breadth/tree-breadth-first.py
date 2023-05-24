from node import Node
class Binary_search_tree():
    def __init__(self):
        self.root=None
    def add(self,value,temp=None):
        """this method used to add a node on the tree on the left or the the right depending on its value """
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
    def tree_breadth_first(self,arg=None,resu=None):
        if(resu is None):
            resu = []
        if(arg==None):
            arg=self.root
            resu.append(self.root.value)
        if(arg):
            if(arg.left):
                self.in_order(arg.left,resu)
            resu.append(arg.value)
            if(arg.right):
                self.in_order(arg.right,resu)
        if(arg == self.root):
            return resu       