def solution(arr):
    result = []
    for num in arr:
        result.extend([num] * num)
    return result