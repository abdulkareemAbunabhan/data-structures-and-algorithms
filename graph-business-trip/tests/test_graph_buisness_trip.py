import pytest
from graphh import *
from graph_business_trip import business_trip
def test_business_trip():
    grd=Graph()
    Pandora=grd.add_vertex("Pandora")
    Arendelle=grd.add_vertex("Arendelle")
    Metroville=grd.add_vertex("Metroville")
    Monstroplolis=grd.add_vertex("Monstroplolis")
    Narnia=grd.add_vertex("Narnia")
    Naboo=grd.add_vertex("Naboo")
    grd.add_edge(Pandora,Arendelle,150)
    grd.add_edge(Pandora,Metroville,82)
    grd.add_edge(Arendelle,Metroville,99)
    grd.add_edge(Arendelle,Monstroplolis,42)
    grd.add_edge(Metroville,Monstroplolis,105)
    grd.add_edge(Metroville,Narnia,37)
    grd.add_edge(Metroville,Naboo,26)
    grd.add_edge(Monstroplolis,Naboo,73)
    grd.add_edge(Naboo,Narnia,250)
    assert business_trip(grd,["Metroville", "Pandora"])== 82
    assert business_trip(grd,["Arendelle","Monstroplolis", "Naboo"]) == 115
    assert business_trip(grd,["Naboo", "Pandora"]) == None
    assert business_trip(grd,["Narnia", "Arendelle", "Naboo"]) == None