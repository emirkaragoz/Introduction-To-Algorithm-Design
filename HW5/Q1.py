def jobOrder(jobs):
    wct=0
    time=0
    n = len(jobs)
        
    #sort according to weight/time rate
    for i in range(n): 
        for j in range(0, n-i-1):
            if jobs[j][1]/jobs[j][2] < jobs[j+1][1]/jobs[j+1][2] :
                jobs[j], jobs[j+1] = jobs[j+1], jobs[j]
    
    #compute weighted complexity time
    for i in range(n):
        time+=jobs[i][2]
        wct+= time*jobs[i][1]
    
    return wct
             
arr = [[1,10,1],[2,2,3],[3,4,2]]    #first element job id, second element weight of job, third element time of job
print("Weighted complexity time: ",jobOrder(arr)) 
print ("Job order list:",arr)

