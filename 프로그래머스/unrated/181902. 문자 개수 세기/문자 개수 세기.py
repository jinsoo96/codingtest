
def solution(my_string):
    count_list = [0] * 52
    #ord : 문자를 아스키 코드값으로 변환해주는 코드임 
    # 대문자 0~25 소문자 26~52
    for char in my_string:
        if 'A' <= char <= 'Z':
            count_list[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            count_list[ord(char) - ord('a') + 26] += 1
    
    return count_list