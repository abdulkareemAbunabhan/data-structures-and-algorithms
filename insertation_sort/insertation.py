def insert(sorted,value):
    """this function will take a sorted array and a number to insert in it as an arguments and return the array after
    inserting the number in  the right place"""
    i=0
    while i<len(sorted) and value > sorted[i]:
        i+=1
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i +=1
    sorted.append(value)

def insertionSort(list):
  """this function takes a list as an argument and iterate on each element and send each element to other function
  to return a new sorted array"""
  sorted = []
  sorted.append(list[0])
  for i in range(1,(len(list))):
    insert(sorted, list[i])
  return sorted