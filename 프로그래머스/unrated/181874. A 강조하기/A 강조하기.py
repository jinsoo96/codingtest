def solution(myString):
    # 먼저 "a"를 "A"로 바꿉니다.
    myString = myString.replace('a', 'A')

    # 그 다음에 "A"를 제외한 모든 대문자를 소문자로 바꿉니다.
    answer = ''
    for ch in myString:
        if ch != 'A' and ch.isupper():
            answer += ch.lower()
        else:
            answer += ch
    return answer
