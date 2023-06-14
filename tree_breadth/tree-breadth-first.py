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
    def tree_breadth_first(self,arg=None,resu=None,order=0):
        """this method is used to traverse on the tree line by line and return the result in a list"""
        if(resu is None):
            resu = []
        if(arg==None):
            arg=self.root
            resu.append([0,self.root.value])
        if(arg):
            order+=1
            if(arg.left):
                resu.append([order:arg.left.value])
                self.tree_breadth_first(arg.left,resu,order)
            if(arg.right):
                resu.append({order:arg.right.value})
                self.tree_breadth_first(arg.right,resu,order)
        if(arg == self.root):
            resu.sort()
            result=[]
            for i in resu:
                result.append(i.value)
            return result

tes=Binary_search_tree()
tes.add(15)
tes.add(5)
tes.add(25)
tes.add(3)
tes.add(7)
tes.add(23)
tes.add(27)
tes.tree_breadth_first()