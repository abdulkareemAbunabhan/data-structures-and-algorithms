def insertShiftArray(arr,num):
    resArr=[]
    for i in range(len(arr)+1):
        if len(arr)%2==1:
          if i< (len(arr)/2) + 0.5:
           resArr[i]=arr[i]
          elif i== (len(arr)/2) + 0.5:
                resArr[i]=num
                i-=1
          else:
             resArr[i]=arr[i-1]
        else:
           if i < len(arr):
              resArr[i]=arr[i]
           elif i == len(arr):
              resArr[i]=num
           else:resArr[i]=arr[i-1]

    return resArr         