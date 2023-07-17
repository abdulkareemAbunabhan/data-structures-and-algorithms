def left_join(first_hashmap,second_hashmap):
    """this function is responsible on doing left join on two hash tables and return the result is list of lists"""
    result=[]
    if first_hashmap == {}:
        return result
    else:
        for i in first_hashmap:
            if i in second_hashmap:
                result.append([i,first_hashmap[i],second_hashmap[i]])
            else:
                result.append([i,first_hashmap[i],None])
        return result