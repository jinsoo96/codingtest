def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow**(1/2))+1):
        if yellow %i ==0:
            if 2*(i+yellow//i) == brown-4:
                answer.append(yellow//i+2)
                answer.append(i+2)
                
    return answer