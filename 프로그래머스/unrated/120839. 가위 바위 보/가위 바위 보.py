def solution(rsp):
    answer = ''
    d = {'0':'5','5':'2','2':'0'}
    answer = ''.join([d[i] for i in rsp])
           
       
    return answer