def solution(my_string, m, c):
    result = ""
    length = len(my_string)
    for i in range(0, length, m):
        result += my_string[i + c - 1]

    return result