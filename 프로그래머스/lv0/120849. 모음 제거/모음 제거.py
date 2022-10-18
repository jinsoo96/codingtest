def solution(my_string):
    answer = my_string
    mo = ('a', 'e', 'i', 'o', 'u')
    for x in my_string.lower():
        if x in mo:
            answer = answer.replace(x, '')
    return answer