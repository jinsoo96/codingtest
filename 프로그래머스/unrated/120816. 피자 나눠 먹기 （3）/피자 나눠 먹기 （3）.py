def solution(slice, n):
    answer = 1
    piece = slice 
    for i in range(n):
        if (answer*slice)/n >= 1:
            break
        else:
            answer+=1
    return answer