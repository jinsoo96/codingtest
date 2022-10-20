def solution(sides):
    answer = 0
    a = max(sides)
    sides.remove(a)
    k = sum([ i for i in sides])
    if a<k:
        answer = 1
    else:
        answer = 2
    return answer