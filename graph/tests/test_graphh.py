import pytest
from graphh import Graph

# 1-Vertex can be successfully added to the graph
def test_add():
    gre=Graph()
    gre.add_vertex("S")
    assert gre.__str__()=="S---->\n"

# 2- An edge can be successfully added to the graph
def test_add_edge():
    gra=Graph()
    vert1=gra.add_vertex("A")
    vert2=gra.add_vertex("B")
    gra.add_edge(vert1,vert2)
    assert gra.__str__()=="A---->(B,0)-->\nB---->(A,0)-->\n"
# 3- A collection of all vertices can be properly retrieved from the graph
def test_all_keys():
    grs=Graph()
    grs.add_vertex("F")
    grs.add_vertex("B")
    grs.add_vertex("A")
    grs.add_vertex("C")
    grs.add_vertex("D")
    grs.add_vertex("E")
    assert grs.get_vertics()==grs.adju_list.keys()
# 4- All appropriate neighbors can be retrieved from the graph
def test_retrive_neighbors():
    grd=Graph()
    A=grd.add_vertex("A")
    B=grd.add_vertex("B")
    C=grd.add_vertex("C")
    D=grd.add_vertex("D")
    grd.add_edge(A,D)
    grd.add_edge(A,C)
    assert grd.get_neighbors(A)==[['D', 0], ['C', 0]]
# 5- Neighbors are returned with the weight between vertices included
def test_neighb():
    gta=Graph()
    A=gta.add_vertex("A")
    B=gta.add_vertex("B")
    C=gta.add_vertex("C")
    D=gta.add_vertex("D")
    gta.add_edge(A,D,5)
    gta.add_edge(A,B,3)
    gta.add_edge(C,B,7)
    assert gta.get_neighbors(B)==[['A', 3], ['C', 7]]
# 6- The proper size is returned, representing the number of vertices in the graph
def test_size():
    gta=Graph()
    A=gta.add_vertex("A")
    B=gta.add_vertex("B")
    C=gta.add_vertex("C")
    D=gta.add_vertex("D")
    gta.add_edge(A,D,5)
    gta.add_edge(A,B,3)
    gta.add_edge(C,B,7)
    assert gta.size()==4
# 7- A graph with only one vertex and edge can be properly returned
def test_one_only():
    gta=Graph()
    A=gta.add_vertex("A")
    assert gta.__str__()=="A---->\n"