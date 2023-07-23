def business_trip(graph,cities):
    """this function tekes a graph and list of cities as arguments and return the cost of trip between those cities in the right order"""
    cities_in_graph={}
    for i in graph.adju_list.keys():
        cities_in_graph[i.value]=i
    cost_of_the_trip=0
    for i in range(len(cities)-1):
        if cities[i] not in cities_in_graph:
            return None
        elif graph.adju_list[cities_in_graph[cities[i]]] == []:
            return None
        else:
            for j in graph.adju_list[cities_in_graph[cities[i]]]:
                if j.vertex.value == cities[i+1]:
                    cost_of_the_trip+=j.weight
            if cost_of_the_trip == 0:
                return None
    return cost_of_the_trip