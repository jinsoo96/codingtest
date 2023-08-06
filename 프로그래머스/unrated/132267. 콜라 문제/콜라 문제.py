def solution(a, b, n):
    answer = 0

    while n >= a:
        e, d = divmod(n, a)
        answer += e * b
        n = e * b + d

    return answer
