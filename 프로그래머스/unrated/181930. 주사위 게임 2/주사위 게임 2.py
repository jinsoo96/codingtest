def solution(a, b, c):
    answer = 0
    total = a+b+c
    if a==b==c:
        answer += total*(a**2+b**2+c**2)*(a**3+b**3+c**3) 
    elif a==b or a==c or b==c:
        answer += total*(a**2+b**2+c**2)
    else:
        answer+=total
    return answer