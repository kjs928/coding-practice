def solution(number, n, m):
    if (number%m==0) and (number%n==0):
        answer=1
    else:
        answer=0
    return answer