import math
import os
import random
import re
import sys


def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    n = len(arr)
    for i in arr:
        if i == 0:
            zero += 1
        if i > 0:
            pos +=1
        if i < 0:
            neg +=1
    pos1 = pos/n 
    neg1 = neg/n
    zero1 = zero/n
    print('%.5f'%pos1)
    print('%.5f'%neg1)
    print('%.5f'%zero1)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
