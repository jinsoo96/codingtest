def solution(babbling):
    # 조카가 발음할 수 있는 기본 발음
    sounds = ["aya", "ye", "woo", "ma"]
    
    # 문자열이 주어진 발음 조합으로 만들어질 수 있는지 확인
    def can_make_sound(s):
        while s:
            found = False
            for sound in sounds:
                if s.startswith(sound):
                    s = s[len(sound):]
                    found = True
                    break
            # 현재 문자열이 어떤 발음으로도 시작하지 않는 경우
            if not found:
                return False
        return True

    # 문자열 내에 연속된 발음이 있는지 확인
    def has_consecutive_sound(s):
        for sound in sounds:
            if sound * 2 in s:
                return True
        return False

    count = 0
    for word in babbling:
        if can_make_sound(word) and not has_consecutive_sound(word):
            count += 1
            
    return count
