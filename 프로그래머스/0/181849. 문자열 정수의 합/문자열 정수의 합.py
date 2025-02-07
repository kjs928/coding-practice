def solution(num_str):
    a=list(num_str)
    answer = 0
    for i in a:
        answer+=int(i)
    return answer