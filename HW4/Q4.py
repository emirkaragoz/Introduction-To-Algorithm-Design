def partyInvitees(peopleL,pairL):
    whoDeserve=[]   #people who joined party
    people_dic=dict()   #people recognize graph
    for i in peopleL:   #add all people in graph
        people_dic.setdefault(i,[])
    for a,b in pairL:   #add adjacency list of all person
        people_dic[a].append(b)
        people_dic[b].append(a)
    
    for i in peopleList:
        if(len(people_dic[i])<5 or (len(peopleL)-len(people_dic[i])-1)<5): #if 5 know and 5 unkown he/she derserve to join party
            people_dic[i].clear()
    
    for i in people_dic:
        for j in people_dic[i]:
            if(len(people_dic[j]) == 0):    #remove everybody who can't join party from each lists
                people_dic[i].remove(j)
    
    for i in people_dic:
        if(len(people_dic[i])>=5 and (len(peopleL)-len(people_dic[i])-1)>=5):  #determine joining people of party
            whoDeserve.append(i)

    return whoDeserve
    
peopleList = [1,2,3,4,5,6,7,8,9,10,11] #numbers represents people
#1-2-3-4-5-6 know each others and don't know 7-8-9-10-11
peoplePairList =[(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6),(7,8),(8,9),(9,10)]

print(partyInvitees(peopleList,peoplePairList))
            