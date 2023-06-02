def solution(myString, pat):
    # "A"를 "B"로, "B"를 "A"로 바꾼 문자열을 생성합니다.
    converted_string = myString.replace("A", "X").replace("B", "A").replace("X", "B")

    # pat과 일치하는 부분 문자열이 있는지 확인합니다.
    if pat in converted_string:
        return 1
    else:
        return 0
