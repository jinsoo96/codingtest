def solution(num_list):
    answer  = [-1]
    a= -1
    for idx, num in enumerate(num_list):
        if num < 0:
            answer.append(idx)
    
    if len(answer) >1:
        a = answer[1]
        

    
        
    return a