def solution(arr, n):
    for i in range(len(arr)):
        if len(arr) % 2 == 1 and i % 2 == 0:  # arr의 길이가 홀수이고, 짝수 인덱스인 경우
            arr[i] += n
        elif len(arr) % 2 == 0 and i % 2 == 1:  # arr의 길이가 짝수이고, 홀수 인덱스인 경우
            arr[i] += n
    
    return arr
