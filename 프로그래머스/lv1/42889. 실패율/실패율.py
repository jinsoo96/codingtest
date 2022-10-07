# 참가와 실패를 구분한다.
def solution(N, stages):
    answer = []
    len_stages = len(stages)
    len_clear = [0 for _ in range(N+2)]
    for i in stages:
        len_clear[i]+=1
    
    
    
    stage_ing = []
    inguser = len_stages 
    
    
    
    # 도전자의 수는 스테이지 수의 길이
    for ind , looser in enumerate(len_clear): # 01 11 21 31 41 51 
        if ind in [0,N+1]:
            continue
        if inguser ==0:
            stage_ing.append((ind,0))  
            continue
        stage_ing.append((ind,looser/inguser))
        inguser -= looser # 길이줄여서 다시 위 포문으로 돌려버리기 
        
        
        
    stage_ing = sorted(stage_ing,key = lambda info : (-info[1],info[0])) #실패율 정렬 
    
    for info in stage_ing:
        answer.append(info[0]) #뒤집음
        
        
        
    return answer