import random

def nim (n,m):
    player=1
    while(n != 0):
        if(n==m+1):	#extra base control
            return 1 if player==2 else 2
        if(n%m == 0):#default move
            n-=1
        else:	#sensible move
            n-=n%m
        player=1 if player == 2 else 2	#player swicth
    return player 	#winner player

#tests
print("Player",nim(30,3), "is winner!")	#1 player winner
print("Player",nim(49,9), "is winner!") #2 player winner