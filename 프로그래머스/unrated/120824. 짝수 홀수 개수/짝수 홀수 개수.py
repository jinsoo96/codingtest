def solution(num_list):
    even = []
    odds = []
    answer = []
    for i in num_list:
        if i %2 ==0:
            even.append(i)
        elif i%2 ==1 :
            odds.append(i)
    answer.append(len(even))
    answer.append(len(odds))
    
    return answer