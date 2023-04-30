def solution(a, d, included):
    total = 0
    for i, is_included in enumerate(included):
        if is_included:
            total += a + d * i
    return total