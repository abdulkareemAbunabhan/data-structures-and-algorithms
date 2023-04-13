def reversArray(arr):
    rev_arr=[None]*len(arr)
    j=len(arr)-1
    for n in arr:
       rev_arr[j]=n
       j-=1
    return rev_arr

arr=[1,2,3,4,5]
print(reversArray(arr))
