def solution(n):
    ns = bin(n).count("1")
    for i in range(n+1,1000001):
        if ns == bin(i).count("1"):
             break
                
        
        
    return i