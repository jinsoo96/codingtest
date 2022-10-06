#n 0<= <=3000
#나누었을때 나머지값이 0
# 조건을 만족못하면 그냥 출력
# 약수는 최대 자기자신 
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i ==0 :
            answer += i 
        
    return answer
