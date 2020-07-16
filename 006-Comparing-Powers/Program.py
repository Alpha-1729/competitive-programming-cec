#!/usr/bin/python3
# Comparing-Powers

"""
>>>>STEPS:
        taking the log of the both and compare.
>>>>
>>>>
>>>>
>>>>
"""
import math
def takeLog(b,p):
    return p * math.log(b)
b1,p1,b2,p2=map(int,input().split())
if ( takeLog(b1,p1) > takeLog(b2,p2)):print("{}^{} is greater".format(b1,p1))
elif (takeLog(b1,p1) < takeLog(b2,p2)):print("{}^{} is greater".format(b2,p2))
else:print("Both are equal."); 
