#!/usr/bin/python3
# Fiz-Buzz

"""
>>>>STEPS:
        Made a dictionary.
        First add multiples of the number in list "C" as key and value as corresponding word in the list "W".
        If same multiple appear, concatenate it with the existing value in the dictionary.
        Made a final list and iterate i from 1-101 and fill it with:
            value in dic, if key is in dic.
            str(i), else
        And done join method in python.
        
"""
N=int(input())
C=list(map(int,(input().split())))
W=input().split()
dic={}
limit=100
for i in range(N):
    for j in range(C[i],limit+1,C[i]):
        if j in dic:
                dic[j]=dic[j] + " " + W[i]
        else:
                dic[j]=W[i]
            
# For horizontal printing.
# print(', '.join([dic[i] if i in dic else str(i) for i in range(1,limit+1)]))

# OR

# For vertical printing
for i in range(1,limit+1):
    dic.setdefault(i,str(i)) # If key not in dic, add new key and value.
    print(dic[i])
