def isSatisfied(arr,ruleDic):
    for i in ruleDic:
        if(ruleDic.get(i)<0):   # not equal case
            if(arr[i] == arr[-ruleDic.get(i)]):
                return False
        else:   #equal case
            if(arr[i] != arr[ruleDic.get(i)]):
                return False
    return True
    
    
dic ={  
  0:2,  #0 = 2
  1:-3  #1 != 3
}
arr=[5,2,5,7]
print(isSatisfied(arr,dic)) #returns true

dic[1]=3    # 1=3
print(isSatisfied(arr,dic)) #returns false
