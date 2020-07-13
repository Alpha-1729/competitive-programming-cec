#!/usr/bin/python3
# Lattice

"""
>>>>STEPS:
        If the row and column is 5 and 7:
            Then total ways is (5+7)!/((5!*7!))
            After simplification.
            Which became (8*9*10*11*12)/(1*2*3*4*5)
            numerator is (8*9*10*11*12) and denominator is (1*2*3*4*5)

            Here less=5, high=7
            so loop i starts from 1-5:
                numerator*=(high+i) -> same as 8*9*10*11*12
                if numerator%i==0:
                    numerator//=i
                else:
                denominator*=i      -> same as 1*2*3*4*5
                
            return numerator//denominator
>>>>
>>>>
>>>>
>>>>
"""
def totalWays(row,col):
    numerator=denominator=1
    less=min(row,col)
    high=max(row,col)
    for i in range(1,less+1):
        numerator*=(high+i)
        # Simplifying the numerator.
        if numerator%i==0:
            numerator//=i
        else:
            denominator*=i
    return numerator//denominator

row,col=map(int,input().split())
print(totalWays(row,col)) 
    
