#!/bin/python3

import math
import os
import random
import re
import sys
#######################################################################################################
# https://www.hackerrank.com/contests/target-codevita-1/challenges/divisible-sum-pairs
#######################################################################################################
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    # Function to compute the divisible sum pair with three arguments (no. of elements, divisor, list of elements)
    
    # initially, take a count variable as zero
    count=0
    
    #Traverse all elements of the list, one - by - one
    # for loop from 0th index to n-1th index
    for i in range(n):
        # as there is a constraint, i<j
        # here, if i is the last element, then loop terminates
        if i == n-1:
            break       # loop terminate immediately
        else:           # i is not a last element
            # place a nested for loop, to check with every next element
            
            for j in range(i+1,n):
                # as sum of two elements is divisible by 'k' or not
                sum = ar[i]+ar[j]
                
                #if sum exactly divisible by divisor 'k', then increase the value of count
                #count + count + 1
                if sum%k ==0:
                    count+=1
    
    # function will return the value of final count in 'count' variable
    return count
  #######################################################################################################
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Take a input value as n = number of elements in list,  and k = divisor value
    nk = input().split()

    #n = number of elements in list
    n = int(nk[0])

    # k = divisor value
    k = int(nk[1])

    # Take a input list of integer values to check for divisible sum
    ar = list(map(int, input().rstrip().split()))

    # call a function to compute the divisible sum pair with three arguments (no. of elements, divisor, list of elements)
    result = divisibleSumPairs(n, k, ar)

    # Function will return the value in 'result' variable
    fptr.write(str(result) + '\n')
    

    fptr.close()
#######################################################################################################
# https://www.hackerrank.com/contests/target-codevita-1/challenges/divisible-sum-pairs
#######################################################################################################
