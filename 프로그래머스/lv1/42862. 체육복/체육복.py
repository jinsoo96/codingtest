def solution(n, lost, reserve):
    
    answer=0
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for student in set_reserve:
        if student - 1 in set_lost:
            set_lost.remove(student - 1)
        elif student + 1 in set_lost:
            set_lost.remove(student + 1)
    answer = n - len(set_lost)
    return answer
