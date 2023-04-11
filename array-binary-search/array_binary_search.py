def BinarySearch(arr,num):
    l=0
    r=len(arr)-1

    while l<=r :
       m=(l+r)//2
       if arr[m]>num:
          r = m-1
       elif arr[m]<num:
          l=m+1
       else:
          return m
    
    return -1