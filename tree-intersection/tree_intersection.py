from tree import *

def tree_intersection(binary_tree1,binary_tree2):
    """this function takes two binary trees as arguments"""
    hashmap1=HashTable()
    hashmap2=HashTable()
    output_list=[]
    if binary_tree1.root is None or binary_tree2.root is None:
        return []
    else:
         iterate_the_tree(binary_tree1,hashmap1)
         iterate_the_tree(binary_tree2,hashmap2)
         for i in hashmap1.map:
             if i is None:
                  pass
             elif isinstance(i,Linked_list):
                  current=i.head
                  while current:
                       if hashmap2.HasKey(current.value[0]):
                            output_list.append(current.value[0])
                       current=current.next
             elif hashmap2.HasKey(i[0]):
                 output_list.append(i[0])
         return output_list           


def iterate_the_tree(inp_tree,hashap):
    """this function iterates on the trees nodes and append values to a hashmap"""
    if inp_tree.root.left:
        tree=Tree()
        tree.root=inp_tree.root.left
        iterate_the_tree(tree,hashap)
    if inp_tree.root.right:
        tree=Tree()
        tree.root=inp_tree.root.right
        iterate_the_tree(tree,hashap) 
    if(hashap.HasKey(str(inp_tree.root.value))):
            val=hashap.GetKeyValue(inp_tree.root.value)+1
            hashap.Set(inp_tree.root.value,val)
    else:
            hashap.Set(inp_tree.root.value,1)        
