def solution(myStr):
    result = []
    start = 0  # 문자열에서 구분자 탐색 시작 위치

    # 주어진 문자열을 반복하면서 구분자의 위치를 찾습니다.
    for i in range(len(myStr)):
        if myStr[i] in ['a', 'b', 'c']:
            # 구분자 사이에 다른 문자가 있는지 확인합니다.
            if start < i:
                result.append(myStr[start:i])  # 구분자 사이의 문자열을 저장합니다.
            start = i + 1  # 다음 구분자를 탐색하기 위해 시작 위치를 업데이트합니다.

    # 마지막 구분자 이후에 문자열이 있는 경우 저장합니다.
    if start < len(myStr):
        result.append(myStr[start:])

    # 저장한 문자열을 반환합니다.
    if len(result) == 0:
        return ["EMPTY"]
    else:
        return result
