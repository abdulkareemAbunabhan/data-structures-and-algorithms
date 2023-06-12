def insert(sorted,value):
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
  sorted = []
  sorted.append(list[0])
  for i in range(1,(len(list))):
    insert(sorted, list[i])
  return sorted