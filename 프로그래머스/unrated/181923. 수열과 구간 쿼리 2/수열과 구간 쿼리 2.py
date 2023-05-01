def solution(arr, queries):
    answer = []
    for query in queries:
        s,e,k = query
        temp = [x for x in arr[s:e+1] if x>k]
        if temp:
            answer.append(min(temp))
        else:
            answer.append(-1)
    return answer