from itertools import permutations 

def solution(k, dungeons):
    answer = -1 #? 0번 돌수도 있어서? 
    ps = 0 
    ld = len(dungeons) #던전수 
    for i in permutations(dungeons,ld):
        #경우의수 : 순열 
        k1 = k ##k 가 계속 없어져서 원상복귀 
        ps1 = ps
        for p in i:
            if k1>=p[0]:
                k1-=p[1]
                ps1+=1
        answer = max(answer,ps1)  
    # 일정 피로도 사용 던전 탐험
    #최소 칠요 = 던전 탐험 피로 ㅗ20 
    # max 횟수 [[최소필요, 소모필요도]]
    # 최대0 던전 수 
    
    return answer


