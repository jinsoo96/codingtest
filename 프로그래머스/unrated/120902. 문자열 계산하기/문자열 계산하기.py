
# eval 함수 문자열 안에 계산을 해줘벌임
def solution(my_string):
    answer = 0
    string_eval = eval(my_string)
    answer +=string_eval
    return answer