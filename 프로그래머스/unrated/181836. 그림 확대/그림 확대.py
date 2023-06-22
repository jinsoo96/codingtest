def solution(picture, k):
    result = []
    for row in picture:
        temp_row = ''.join([pixel*k for pixel in row])
        for _ in range(k):
            result.append(temp_row)
    return result
