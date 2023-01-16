def solution(quiz):
    answer = []
    for i in quiz:
        a1,b1 = i.split('=')
        a1 = a1.split()
        if a1[1] == "+":
            if int(a1[0])+ int(a1[2]) == int(b1) :
                answer.append("O")
            else:
                 answer.append("X")
        elif a1[1] == "-":
            if int(a1[0]) - int(a1[2]) == int(b1) :
                answer.append("O")
            else:
                answer.append("X")

            
      

            
            
            
            
            
    return answer