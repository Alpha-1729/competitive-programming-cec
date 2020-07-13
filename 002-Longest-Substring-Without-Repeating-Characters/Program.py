#!/usr/bin/python3
# Longest-Substring-Without-Repeating-Characters

"""
>>>>STEPS:
        Made a set.
        loop through all character in the string.
        if character not in string:
            add it to the set
            update length
        else:
            removing from set
        return the length.
>>>>
>>>>
>>>>
>>>>
"""
def maxLength(data):
    store=set()
    length=i=j=0
    while j<len(data):
        if data[j] in store:
            store.remove(data[i])
            i+=1
        else:
            store.add(data[j])
            j+=1
            length=max(len(store),length)
    return length
    
data=input()
print(maxLength(data))   
