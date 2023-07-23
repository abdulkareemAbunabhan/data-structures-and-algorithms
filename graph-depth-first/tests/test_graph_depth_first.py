import pytest
from graph_depth_first import Graph

def test_depth_first():
    grd = Graph()
    A=grd.add_vertex("A")
    B=grd.add_vertex("B")
    C=grd.add_vertex("C")
    D=grd.add_vertex("D")
    E=grd.add_vertex("E")
    F=grd.add_vertex("F")
    G=grd.add_vertex("G")
    H=grd.add_vertex("H")
    grd.add_edge(A,B)
    grd.add_edge(A,D)
    grd.add_edge(B,C)
    grd.add_edge(B,D)
    grd.add_edge(D,E)
    grd.add_edge(D,H)
    grd.add_edge(D,F)
    grd.add_edge(C,G)
    grd.add_edge(H,F)
    assert grd.depth_first(A)== ["A", "B", "C", "G", "D", "E", "H", "F"]