def is_valid(cards1, cards2, goal, idx):
    # 모든 단어를 순서대로 사용한 경우
    if idx == len(goal):
        return True
    
    word = goal[idx]
    
    # cards1에서 word를 사용할 수 있는 경우
    if cards1 and cards1[0] == word and is_valid(cards1[1:], cards2, goal, idx+1):
        return True
    
    # cards2에서 word를 사용할 수 있는 경우
    if cards2 and cards2[0] == word and is_valid(cards1, cards2[1:], goal, idx+1):
        return True
    
    return False


def solution(cards1, cards2, goal):
    if is_valid(cards1, cards2, goal, 0):
        return "Yes"
    else:
        return "No"

