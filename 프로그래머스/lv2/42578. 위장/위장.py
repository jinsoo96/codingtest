def solution(clothes):
    answer = {} #딕셔너리만들기 
    for c in clothes:
        if c[1] in answer:
            answer[c[1]] += 1
        else: 
            answer[c[1]] = 1

    count = 1
    for i in answer.values():
        count *= (i+1)
        
    
    return count-1