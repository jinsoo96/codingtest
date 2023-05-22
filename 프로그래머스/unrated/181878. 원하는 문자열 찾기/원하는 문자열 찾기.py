def solution(myString, pat):
    ml = myString.lower()
    pl = pat.lower()
    if pl in ml:
        return 1
    else:
        return 0