import math
def solution(n):
    if float(math.sqrt(n)).is_integer() == True:
        answer = (math.sqrt(n)+1)**2
    else:
        answer = -1
        
    return answer