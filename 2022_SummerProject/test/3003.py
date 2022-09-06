def solution(para):
    a = '1 1 2 2 2 8'
    answer = ""
    for i in range(len(a)):
        if not para[i] == ' ':
            answer += str(int(a[i]) - int(para[i]))
        else:
            answer += ' '
    return answer