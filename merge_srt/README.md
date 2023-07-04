# Merge sort

* Initial array: [17, 2, 11, 9, 6]
![intial arr](image.png)

* Since the array has more than one element, we proceed with the sorting process.

* Splitting the array into halves:
![two parts](image-1.png)

* Recursively sort the left and right subarrays:
![left text](image-2.png)

* Splitting the left subarray:
![Alt text](image-3.png)

* Since both subarrays have only one element, no further splitting is required.
* Merging the left subarray
![Alt text](image-4.png)

* Recursively sort the left subarrays:
![Alt text](image-6.png)
![Alt text](image-5.png)

* Splitting the right subarray:
![Alt text](image-7.png)

* Recursively sort the right subarray:
* Since both subarrays have only one element, no further splitting is required.
* Merging the left subarray:
    ![Alt text](image-8.png)

* Merging the sorted subarrays:
![Alt text](image-9.png)