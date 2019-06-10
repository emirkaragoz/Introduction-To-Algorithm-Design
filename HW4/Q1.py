def hotelway(way):
    path=[None]*len(way)
    stop=[None]*len(way)
    
    for i in range(len(way)):
        path[i]=pow(200-way[i],2)   #current penalty
        stop[i]=0
        j=0
        while(j<i):
            if((path[j]+pow(200-(way[i]-way[j]),2)) < path[i]): #if next hotel penalty is less than current, penalty chang them
                path[i] = path[j]+pow(200-(way[i]-way[j]),2)
                stop[i]=j+1
            j+=1
        
    finalPath = ""
    index = len(stop)-1
    while(index>=0):    #hotel path like 1-2-3 .. -9
        finalPath = str((index+1))+" "+finalPath
        index = stop[index]-1
    
    return (finalPath,(path[len(way)-1]))
            
A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
x,y = hotelway(A)  
print("Optimal Sequence of Hotels: " +x)
print("Minimum Penalty: "+str(y))
