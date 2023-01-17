def solution(common):
    result = 0 
    a1,a2,a3 = common[:3]
    if (a2-a1) == (a3-a2):
        result = common[-1]+(a3-a2) 
    elif (a2-a1) != (a3-a2):
        result = common[-1] *(a3//a2)
    return result