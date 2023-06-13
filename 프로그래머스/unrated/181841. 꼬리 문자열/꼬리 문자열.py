def solution(str_list, ex):
    tail_str = ""
    
    for s in str_list:
        if ex not in s:
            tail_str += s
    
    return tail_str
