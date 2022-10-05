# 333%10 3 333//10 33 
#6969%10 9 6969//10 
def solution(n):
    answer= 0
    k = list(map(int,str(n)))
    
    for i in range(len(k)):
        answer += k[i]
    
    return answer