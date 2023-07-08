from tree import Tree
def tree_intersection(binary_tree1,binary_tree2):
    """this function takes two binary trees as arguments"""
    hashmap1={}
    hashmap2={}
    output_list=[]
    if binary_tree1.root is None or binary_tree2.root is None:
        return []
    else:
         iterate_the_tree(binary_tree1,hashmap1)
         iterate_the_tree(binary_tree2,hashmap2)
    for i in hashmap1:
         if i in hashmap2:
            output_list.append(i)
    return output_list           


def iterate_the_tree(inp_tree,hashmap):
    """this function iterates on the trees nodes and append values to a hashmap"""
    if inp_tree.root.left:
        tree=Tree()
        tree.root=inp_tree.root.left
        iterate_the_tree(tree,hashmap)
    if inp_tree.root.right:
        tree=Tree()
        tree.root=inp_tree.root.right
        iterate_the_tree(tree,hashmap) 
    if(inp_tree.root.value in hashmap):
            hashmap[inp_tree.root.value]+=1
    else:
            hashmap[inp_tree.root.value]=1        
