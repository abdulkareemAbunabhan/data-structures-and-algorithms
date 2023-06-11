

def insert(sorted,value):
    i=0
    while i<len(sorted) and value > sorted[i]:
        i+=1
    sorted.append(None)    
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i +=1
    sorted[len(sorted)-1]=(value)

def insertionSort(list):
  sorte = [0]
  sorte[0] = list[0]
  for i in range(1,len(list)):
    insert(sorte, list[i])
  return sorte