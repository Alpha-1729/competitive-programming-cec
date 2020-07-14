#!/usr/bin/python3
# Last-Ten-Digit

"""
>>>>pow with 3 arguments (base,power,modulo)
>>>>Actual implementation:
        link: https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
>>>>
>>>>
>>>>
"""
a,b=map(int,input().split())
print(pow(a,b,10**10))
