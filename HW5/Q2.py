#Q2-a
def incorrectOptimalCost(n,M,NY,SF):	#just consider monthly cost
    cost=0								#doesn't consider moving cost(m)
    for i in range(0,n):
        if(NY[i]<SF[i]):
            cost+=NY[i]
        else:
            cost+=SF[i]
            
    return cost

#Q2-b
def optimalCost(n,M,NY,SF):
	#initial values
    optimumNY=[NY[0]]*n
    optimumSF=[SF[0]]*n

    for i in range(1,n):
        optimumNY[i] = NY[i]+ min(optimumNY[i-1], M + optimumSF[i-1])	#choose minimum of current NY cost or movining cost + current SF cost
        optimumSF[i] = SF[i]+ min(optimumSF[i-1], M + optimumNY[i-1])	#choose minimum of current SF cost or movining cost + current NY cost
    
    return(min(optimumNY[n-1],optimumSF[n-1]))  #choose minimum of NY or SF cost


print("Incorrenct Optimum Cost: ",incorrectOptimalCost(4,100,[1,30,20,30],[50,20,21,4]))	#Q2-a
print("Correnct Optimum Cost: ",optimalCost(4,20,[1,30,20,30],[50,20,21,4]))                #Q2-b   
