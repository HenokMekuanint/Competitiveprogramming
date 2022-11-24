#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minNum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER samDaily
#  2. INTEGER kellyDaily
#  3. INTEGER difference
#  sam     3+6= 9
# 3 kelly=  6
# 6 diff=   6
# 6
def minNum(samDaily, kellyDaily, difference):
    # Write your code here
    samsolved=samDaily+difference
    kellysolved=kellyDaily
    if kellyDaily>=samsolved:
        return -1
    else:
        days=1
        while samsolved>kellysolved:
            samsolved+=difference
            kellysolved+=kellyDaily
            days+=1
    return days
            
if __name__ == '__main__':
