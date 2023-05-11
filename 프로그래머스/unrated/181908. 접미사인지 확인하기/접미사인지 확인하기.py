def solution(my_string, is_suffix):
    answer = 0
    i_ = len(is_suffix)
    if (my_string[len(my_string)-i_:len(my_string)]) == is_suffix:
        answer +=1
    else:
        answer = 0
        
    return answer
  
        
    
    
    
    
    return answer