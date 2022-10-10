from math import gcd

def solution(denum1,num1,denum2,num2):
    answer = []
    denum = denum1*num2 + denum2*num1
    num = num1*num2
    a,b = denum//gcd(denum,num), num//gcd(denum,num)
    
    answer.append(a)
    answer.append(b)

    return answer
