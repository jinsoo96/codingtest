def solution(numbers):
    answer = 1
    numbers_sort = sorted(numbers)
    answer = max(numbers_sort[0]*numbers_sort[1],numbers_sort[-1]*numbers_sort[-2])    
    
   
    return answer