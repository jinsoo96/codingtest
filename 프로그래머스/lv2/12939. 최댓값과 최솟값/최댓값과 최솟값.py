def solution(s):
    s = s.split()
    n= [int(i) for i in s]
    answer = str(min(n))+" "+ str(max(n))
    
    return answer