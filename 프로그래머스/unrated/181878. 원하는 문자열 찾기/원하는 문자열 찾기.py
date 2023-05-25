def solution(myString, pat):
    answer = 0
    ml = myString.lower()
    pl = pat.lower()
    if pl in ml:
        answer = 1 
    else:
        answer = 0
        
    return answer 