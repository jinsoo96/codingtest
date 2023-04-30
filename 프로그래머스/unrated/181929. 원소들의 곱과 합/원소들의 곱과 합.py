def solution(num_list):
    answer = 0
    a=1
    b=0
    for i in num_list:
        a *=i
    for j in num_list:
        b +=j
    
    if a <b**2 :
        answer+=1
    elif a>b**2 : 
        answer=0
    return answer