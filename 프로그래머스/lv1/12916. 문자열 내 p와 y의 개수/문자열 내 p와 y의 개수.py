def solution(s):
    a= s.lower()
    if a.count('p')==a.count('y'): 
        answer = True
    elif a.count('p')!=a.count('y'):
        answer = False
    else:
        answer = True
        
    return answer