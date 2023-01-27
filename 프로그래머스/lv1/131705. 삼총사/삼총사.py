from itertools import combinations

def solution(number):
    len_an = []
    
    c_num =  list(combinations(number,3))
    

    for i in c_num:
        
        if sum(i)==0:
            len_an.append(i)
                                                   
                          
    answer = len(len_an)
            
            
    
    return answer