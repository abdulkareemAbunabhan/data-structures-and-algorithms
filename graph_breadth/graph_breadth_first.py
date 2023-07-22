from node import *
class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex=vertex
        self.weight=weight
    
    def __str__(self):
        return (self.vertex.value,self.weight)

class Graph:
    def __init__(self):
        """this function is regarding initiating instance from the class with a list"""
        self.adju_list={}

    def add_vertex(self,value):
        """this function is responsable to add node to the graph"""
        vertex=Node(value)
        self.adju_list[vertex]=[]
        return vertex
    
    def add_edge(self,vert1,vert2,weight=0):
        """this function is responsable tp add an edge to the graph"""
        if not vert1 in self.adju_list:
            return(f'{vert1} is not in the graph')
        if not vert2 in self.adju_list:
            return (f'{vert2} is not on the graph')
        edge1=Edge(vert2,weight)
        edge2=Edge(vert1,weight)
        self.adju_list[vert1].append(edge1)
        self.adju_list[vert2].append(edge2)

    def get_vertics(self):
        """this function returns all the vertex in the graph"""
        return self.adju_list.keys()
    
    def get_neighbors(self,vertex):
        """this function return all the neighbors of input vertex"""
        res=[]
        if not vertex in self.adju_list:
            return f'{vertex} is not in the graph'
        else:
            for i in self.adju_list[vertex]:
                res.append([i.vertex.value,i.weight])
        return res
    
    def size(self):
        """this function is responsable of returning the size of the graph"""
        return len(self.adju_list)
    
    def breadth_first(self, node):
        """this method is used to traverse a graph level by level starting from a givin node"""
        result = {}
        queue = Queue()

        queue.enqueue(node)

        while not queue.isEmpty():
            current_node = queue.dequeue()
            if current_node.value not in result:
                result[current_node.value] = current_node

            edges = self.adju_list[current_node]
            for edge in edges:
                neighbor = edge.vertex
                if neighbor.value not in result:
                    queue.enqueue(neighbor)
        return list(result.keys())    
        

    def __str__(self):
        """this method used to return a string of what in the graph"""
        output=''
        for i in self.adju_list:
            output+=f'{i}---->'
            for i in self.adju_list[i]:
                output+=f'({i.vertex.value},{i.weight})-->'
            output+="\n"
        return output