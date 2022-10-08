#인덱스를 이용한 길이별 함수 사용 하기 
def solution(phone_number):
    answer = "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer