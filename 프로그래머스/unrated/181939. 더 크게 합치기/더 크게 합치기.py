def zerox(a,b):
    return int(str(a)+str(b))

def zeroy(a,b):
    return int(str(b)+str(a))


def solution(a, b):
    answer = 0
    if zerox(a,b) >= zeroy(a,b):
        answer +=zerox(a,b)
    else:
        answer +=zeroy(a,b)
    
    return answer