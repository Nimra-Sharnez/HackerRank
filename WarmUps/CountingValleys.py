#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.

def countingValleys(n, s):
    height=0
    valley=0
    tracker=[]
    for i in range(len(s)):
        if (s[i]=="U"):
            height+=1
        elif(s[i]=="D"):
            height-=1
        tracker.append(height)


    for j in range(1, len(tracker)):
        if(tracker[j]==0 and tracker[j-1]<0): #if we are at sea level, and before we were below
            valley+=1 #we just came out of a valley
            
    return(valley)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
