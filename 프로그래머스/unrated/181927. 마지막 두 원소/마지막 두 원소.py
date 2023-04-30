def solution(num_list):
    le = num_list[-1]
    sle = num_list[-2]
    if le >sle :
        num_list.append(le-sle)
    else:
        num_list.append(le*2)
    return num_list