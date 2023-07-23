import pytest
from graph_breadth_first import Graph
def test_breadth_first():
    grd=Graph()
    Pandora=grd.add_vertex("Pandora")
    Arendelle=grd.add_vertex("Arendelle")
    Metroville=grd.add_vertex("Metroville")
    Monstroplolis=grd.add_vertex("Monstroplolis")
    Narnia=grd.add_vertex("Narnia")
    Naboo=grd.add_vertex("Naboo")
    grd.add_edge(Pandora,Arendelle)
    grd.add_edge(Arendelle,Metroville)
    grd.add_edge(Arendelle,Monstroplolis)
    grd.add_edge(Metroville,Monstroplolis)
    grd.add_edge(Metroville,Narnia)
    grd.add_edge(Metroville,Naboo)
    grd.add_edge(Monstroplolis,Naboo)
    grd.add_edge(Naboo,Narnia)
    assert grd.breadth_first(Pandora)==['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']