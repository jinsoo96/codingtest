def solution(price):
    answer = 1
    if 100000<=price<300000:
        answer *= int(price*0.95)
    elif 300000<=price<500000:
        answer *= int(price*0.9)
    elif price >=500000:
        answer *= int(price*0.8)
    elif price<100000:
        answer *=int(price*1)
    
    
    return answer