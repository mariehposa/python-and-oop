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
