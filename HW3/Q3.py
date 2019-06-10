def binarySearch (arr, mini, maxi, target):
    if maxi >= mini:
        mid = mini + (maxi - mini)//2
        if arr[mid] == target and mid == target: #arr[i] == i 
            return mid

        elif arr[mid] > target: #left side
            return binarySearch(arr, mini, mid-1, target)

        else:   #right side
            return binarySearch(arr, mid + 1, maxi, target)
    else:
        return -1

#test
arr = [0,1,2,3,5]
t = 3

result = binarySearch(arr, 1, len(arr), t)
if result != -1:
    print ("arr[", result,"] = ",result)
else:
    print ("There is not arr[i] = i")
