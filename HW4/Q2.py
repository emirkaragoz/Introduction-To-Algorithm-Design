def reconstituter (text,wset):
    start=0
    end=1
    returntext=""
    for i in range (len(text)):
        key = text[start:end] #[0:1],[0:2],.. [0:n] until key matches a word in word set
        if (end == len(text)+1):    #end of text
            break
        if(key in wset): 
            start=end
            end+=1
            returntext+=key+" " #found,add to return text
            key=[]  #reset key
        else:
            end+=1  #increase end [ :end+=1]
    
    if(len(key) == 0):  #key must empty if text created by words in word set
        return (True,returntext)
    return (False,returntext)   #otherwise,false

word_set={"it","was","the","best","of","times"}
text1="itwasthebestoftimes"
x,y = reconstituter(text1,word_set)
if(x):
    print(y)
