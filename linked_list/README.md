# linked list

Create a Linked List class, Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created. The class should contain the following methods
insert, includes and to_string

## Whiteboard Process

![whiteBoard](array_binary_search.png)

## Approach & Efficiency

time complexity O(log n) Space complexity O(1)

## Solution

<pre>

 ``` python
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
 ```
</pre>