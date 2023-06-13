from collections import defaultdict

def solution(strArr):
    groups = defaultdict(int)  # 그룹별 개수를 저장할 딕셔너리

    # 문자열을 그룹별로 나누어 개수를 카운트
    for s in strArr:
        groups[len(s)] += 1

    max_count = max(groups.values())  # 최대 개수

    return max_count
