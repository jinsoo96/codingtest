def factorial(m):
        if m == 0:
            return 1
        else:
            return m * factorial(m-1) #팩토리얼 정의함수
def solution(n):
    i = 0
    while factorial(i) <= n:
        i += 1
    return i - 1