def solution(num_list):
    sorted_list = sorted(num_list)  # num_list를 정렬
    result = sorted_list[5:]  # 정렬된 리스트에서 6번째 이후의 수들을 선택하여 결과 리스트에 저장
    
    return result
