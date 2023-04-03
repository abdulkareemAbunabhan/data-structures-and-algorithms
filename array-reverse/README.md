# Array Reverse

Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Whiteboard Process
[whiteBoardPic](./pics/Capture.PNG)

## Approach & Efficiency

my code will iterate on the given array and insert the value of each item in the begging of the new array.

## Solution

<pre>
```python
def reversArray(arr):
    rev_arr=[]
    for n in arr:
       rev_arr.insert(0,n)
    return rev_arr
arr=[1,2,3,4,5]
print(reversArray(arr))
```
</pre>
