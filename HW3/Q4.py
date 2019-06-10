def maxSum(arr, low, mid, high) : 
    total = 0; left_total = -1000000
      
    #left of mid
    for i in range(mid, low-1, -1) : 
        total = total + arr[i] 
        if (total > left_total) : 
            left_total = total 
      
    #right of mid
    total = 0; right_total = -1000000
    for i in range(mid + 1, high + 1) : 
        total = total + arr[i] 
        if (total > right_total) : 
            right_total = total 
      
    return left_total + right_total; 
  
def maxSubArrTotal(arr, low, high) : 
    #just one element arr
    if (low == high) : 
        return arr[low] 
 
    #middle point
    mid = (low + high) // 2
  
    return max(maxSubArrTotal(arr, mid+1, high),    #max subarray total in right half 
               maxSubArrTotal(arr, low, mid),       #max subarray total in left half 
               maxSum(arr, low, mid, high))         #max subarray total passing midpoint
      
#test        
arr = [2,3,4,-10,5,9,-10,7] 
  
max_total = maxSubArrTotal(arr, 0, len(arr)-1) 
print("Largest sum of contiguous subset is ", max_total) 