
def left_join(first_hashmap, second_hashmap):
    """this function is responsible for doing left join on two hash tables and returning the result as a list of lists"""
    result = []
    
    for key in first_hashmap.AllKeys():
        value = first_hashmap.GetKeyValue(key)
        antonym_value = second_hashmap.GetKeyValue(key)
        result.append([key, value, antonym_value])
        
    return result