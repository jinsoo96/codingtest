import math
import numpy as np
def solution(n):
    answer = 0
    a = math.sqrt(n) 
    if a ==int(a) :
        answer = 1
    else:
        answer = 2
    return answer