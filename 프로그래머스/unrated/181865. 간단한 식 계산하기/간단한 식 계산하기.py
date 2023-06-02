def solution(binomial):
    # 이항식을 공백을 기준으로 나누어 피연산자와 연산자를 분리합니다.
    a, op, b = binomial.split()

    # 피연산자를 정수로 변환합니다.
    a = int(a)
    b = int(b)

    # 연산자에 따라 계산을 수행합니다.
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b

    # 계산 결과를 반환합니다.
    return result
