word_dic=dict()
word_set={"to","be","or","not"}
def determine_pattern (text,pattern,wset,dic,symbol,start,end):
    key = text[start:end]
    if (end == len(text)+1):    #base case
        return -1
    if(key in dic): #check key in dict
        start=end
        end+=1
        pattern.append(dic[key]) #add pattern but not add dic again
        determine_pattern(text,pattern,wset,dic,symbol,start,end)
    elif (key in wset): 
        start=end
        end+=1
        pattern.append(symbol)  #add pattern
        dic.setdefault(key,None)
        dic[key]=symbol         #add dict
        symbol=chr(ord(symbol) + 1) #update symbol
        determine_pattern(text,pattern,wset,dic,symbol,start,end)
    else:
        end+=1
        determine_pattern(text,pattern,wset,dic,symbol,start,end)

#compare incoming patter and text's pattern 
def check_pattern(text,pattern,wset):
    pattern_list = []
    determine_pattern(text,pattern_list,wset,word_dic,'A',0,1)
    print(pattern_list,"-",pattern)
    if (pattern_list == pattern):
        return True;
    return False;

#test
pattern=list("ABCDAB")
if(check_pattern("tobeornottobe",pattern,word_set)):
    print("Pattern is correct")
else:
    print("Pattern is incorrect")
 