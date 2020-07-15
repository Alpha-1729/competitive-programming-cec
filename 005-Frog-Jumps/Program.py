#!/usr/bin/python3
# Frog-Jumps

"""
>>>>Simple solution: -> Each line is self explained.
>>>>def willMeet(x1,x2,v1,v2):
    if(x1>=x2 and v1>v2) or (x2>=x1 and v2>v1):
        return "NO"
    elif x1==x2 and v1==v2:
        return "YES"
    elif x1!=x2 and v1==v2:
        return "NO"
    elif abs(x1-x2) % abs(v1-v2)==0:
        return "YES"
    return "NO"
>>>>
>>>>
>>>>
>>>>
"""

def willMeet(x1,x2,v1,v2,text="NO"):
    if(x1 >= x2 and v1 > v2) or (x2 >= x1 and v2 > v1) or (x1 != x2 and v1 == v2) : pass
    elif (x1 == x2 and v1 == v2) or (abs(x1 - x2) % abs(v1 - v2) == 0) : text="YES"
    return text

x1,v1,x2,v2=map(int,input().split())
print(willMeet(x1,x2,v1,v2))
    