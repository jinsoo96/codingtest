from heapq import heappop, heappush

def solution(n, k, enemy):
    heap = []
    s_enemy = 0
    answer = 0
    #answer += len(enemy)-k #heap push 
    for i in enemy:
        s_enemy +=i
        heappush(heap,-i)
        
        
        if s_enemy>n: #초과하는 경우 
            
            if k >0:
                s_enemy +=heappop(heap) 
                k -= 1
            else:
                break
                
            
            
        answer += 1
    # heappop
    # enemy[i] 만큼 소모 
    # 무적권 = k 번 enemy[i]=0 이됨 
    # n <=enemy[i] 일시 종료 
    # 몇 라운드 까지 막을수 있는지 
    # 무적권은 다쓴다 근데 언제 쓸지 모름 
      
    
    return answer