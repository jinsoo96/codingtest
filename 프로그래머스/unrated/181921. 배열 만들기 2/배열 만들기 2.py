def solution(l, r):
    answer = []

    for i in range(l, r+1):
        num_str = str(i)
        if all(j in {'0', '5'} for j in num_str):
            answer.append(i)

    return answer if answer else [-1]

    