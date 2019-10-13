#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs=0

    dictionary = {i:ar.count(i) for i in ar}


    num_socks = list(dictionary.values())

   
    
    for i in range (len(num_socks)):
        if (num_socks[i]%2==0): #is even?
            pairs+= (num_socks[i]/2)
        else:                   #is odd?
            if(num_socks[i]!=1):
                evened = num_socks[i]-1
                pairs+= (evened/2)

    return round(pairs)
                

        
  

        
            



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()