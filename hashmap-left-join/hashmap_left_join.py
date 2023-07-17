from hasher import *
def left_join(first_hashmap,second_hashmap):
    """this function is responsible on doing left join on two hash tables and return the result is list of lists"""
    result=[]
    if first_hashmap.map == []:
        return result
    else:
        for i in first_hashmap.map:
            result.append("s")
            if i is None:
                result.append("a")
                pass
            elif isinstance(i,Linked_list):
                result.append("d")
                current=i.head
                while current:
                    if second_hashmap.HasKey(current.value):
                        result.append[current.value,first_hashmap.GetKeyValue(current.value),second_hashmap.GetKeyValue(current.value)]
                    current=current.next
            elif second_hashmap.HasKey(i[0]):
                result.append("s")
                result.append([i[0],first_hashmap.GetKeyValue(i[0]),second_hashmap.GetKeyValue(i[0])])
            else:
                result.append("e")
                result.append([i[0],first_hashmap.GetKeyValue(i[0]),None])
        return result