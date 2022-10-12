def solution(numbers): # 문자변경, 문자 정렬, 정수변환
    numbers = list(map(str, numbers)) #numbers 1000 자리 
    numbers.sort(key=lambda x: x * 3, reverse=True) #큰수부터 배열 
    answer = str(int(''.join(numbers)))
    return answer