def solution(array):
    count = {}  # 원소의 등장 횟수를 저장할 딕셔너리
    max_count = 0  # 가장 많이 등장한 횟수
    mode = []  # 최빈값을 저장할 리스트

    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] > max_count:
            max_count = count[num]

    for num, freq in count.items():
        if freq == max_count:
            mode.append(num)

    if len(mode) > 1:
        return -1
    else:
        return mode[0]
