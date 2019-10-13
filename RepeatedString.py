#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def aCount(s):
    a=0
    for i in range(len(s)):
        if(s[i]=="a"):
            a+=1
    return(a)

def repeatedString(s, n):
    fit= int(n/len(s))
    
    rem = n-len(s)*fit

    a = aCount(s)
    
    aCounter = a*fit

    tmp=[]
    for j in range(rem):
       tmp.append(s[j]) 
    rA = aCount(tmp)

    aCounter+=rA
    

    return(aCounter)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()