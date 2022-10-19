def solution(my_string):
    answer = ''
    string = my_string.lower()
    answer = answer.join(sorted(string))
    return answer