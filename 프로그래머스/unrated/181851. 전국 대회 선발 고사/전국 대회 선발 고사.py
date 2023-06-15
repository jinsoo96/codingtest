def solution(rank, attendance):
    # 학생 번호와 등수를 쌍으로 묶고, 등수에 따라 오름차순으로 정렬
    rank_with_idx = sorted([(rank[i], i) for i in range(len(rank))])

    selected_students = []
    for _, idx in rank_with_idx:
        # 참가 가능한 학생을 찾았다면 결과 리스트에 추가
        if attendance[idx]:
            selected_students.append(idx)
            # 결과 리스트의 크기가 3이 되면 반복 멈추기
            if len(selected_students) == 3:
                break

    # 결과를 계산하여 반환
    a, b, c = selected_students
    return 10000 * a + 100 * b + c

