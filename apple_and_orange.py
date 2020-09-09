import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    outputA = []
    outputB = []

    for i in range(0, len(apples)):
        resa = a + apples[i]
        if(resa >= s and resa <= t):
            outputA.append(resa)

    for j in range(0, len(oranges)):
        resb = b + oranges[j]
        if(resb >= s and resb <= t):
            outputB.append(resb)

    print(len(outputA))
    print(len(outputB))