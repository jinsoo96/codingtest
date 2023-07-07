def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    result = [sorted_emergency.index(e) + 1 for e in emergency]
    return result
        
#     indexed_emergency = list(enumerate(emergency, 1))

   
#     sorted_emergency = sorted(indexed_emergency, key=lambda x: x[1], reverse=True)

#     priority = [x[0] for x in sorted_emergency]


#     priority.sort(key=lambda x: emergency[x - 1])

    return answer