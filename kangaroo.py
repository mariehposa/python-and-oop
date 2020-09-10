import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if(x2 > x1 and v2 == v1):
        return('NO')
    elif(x2 - x1) % (v2 - v1) == 0 and (x2 - x1) * (v2 - v1) < 0:
        return('YES')
    else:
        return('NO')