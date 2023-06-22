
def solution(order):
    total = 0
    for o in order:
        if o in ["iceamericano", "americanoice", "americano", "anything"]:
            total += 4500
        elif o in ["icecafelatte", "cafelatteice", "cafelatte", "hotcafelatte", "cafelattehot"]:
            total += 5000
        else:
            total += 4500 
    return total




