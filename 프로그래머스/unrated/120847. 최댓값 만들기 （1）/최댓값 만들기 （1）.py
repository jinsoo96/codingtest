def solution(numbers):
    answer = 1
    a = sorted(numbers)
    answer *= a[-1] * a[-2]    
    return answer