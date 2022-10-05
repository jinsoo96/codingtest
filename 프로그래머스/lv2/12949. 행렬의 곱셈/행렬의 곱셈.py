import numpy as np

def solution(arr1, arr2):
    
    answer =  (np.matrix(arr1)*np.matrix(arr2)).tolist()
    
    return answer