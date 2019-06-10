def mergeSort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = mergeSort(arr[:mid]) # Dividing the array elements  
        R = mergeSort(arr[mid:]) # into 2 halves 
      
        return merge(L,R)
    else:
        return arr[0]   #arr size 1
  
       
def merge(left,right):
    if not len(left) or not len(right):     #empty arr check
        return left or right
    result=[]
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):   #clasic merge process
        if left[i] < right[j]:      #for left
            result.append(left[i])
            i+= 1
        else:                       #for right
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):   #long arr increasing element
            result.extend(left[i:] or right[j:])
            break
    return result
        
arr = [[11, 12, 13], [1, 2,3], [101, 102, 111, 125], [11,15,25,56]] 
print ("Given array is: ", arr) 
print("Sorted array is: ", mergeSort(arr)) 
