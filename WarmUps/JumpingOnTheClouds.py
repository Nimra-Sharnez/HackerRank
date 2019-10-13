#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.

def jumpingOnClouds(c):
    safe=[]
    jumps=0
    for i in range(len(c)):
        if(c[i]==0):
            safe.append(i)
    skips = 0
    for i in range(len(safe)):
        if(i<len(safe)-2):
            if(safe[i]+2 == safe[i+2]):
                # skips+=1
                # i+=2
                safe.remove(safe[i+1])
            else:
                jumps+=0
        else:
            jumps+=0
                
    jumps=(len(safe)-1)
    
            

        

    return(jumps)



            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
