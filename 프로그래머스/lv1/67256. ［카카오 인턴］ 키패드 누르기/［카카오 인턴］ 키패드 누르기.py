#두 점간의 맨해튼거리 추출
def dis(a,b):
    a1 = a[0]-b[0]
    a2 = a[1]-b[1]
    if a1<0:
        a1 = -a1
    if a2<0:
        a2 = -a2
    return a1+a2
#결과 반환 LR 반환
def solution(numbers, hand):
    answer = ''
    res= []
    pad = [(1,0)]
    left = (0,0) # *초기
    right = (2,0) # # 초기
    
    for i in range(9):
        pad.append((i%3,3-i//3))  #1은 (1,0) 2는 (2,0) 처럼 표현하기 
        
    length = len(numbers)
    for i in range(length):
        t = numbers[i]
        
        if t==1 or t==4 or t==7:
            res.append("L")
            left = pad[t]
        elif t == 3 or t==6 or t==9:
            res.append("R")
            right = pad[t]
            
        else:
            if(dis(pad[t],left)>dis(pad[t],right)):
                res.append("R")
                right = pad[t]
            elif(dis(pad[t],left)<dis(pad[t],right)):
                res.append("L")
                left = pad[t]
            else:
                if hand[0]=="l":
                    res.append("L")
                    left = pad[t]
                else:
                    res.append("R")
                    right = pad[t]
    answer = ''.join(res)
    return answer
