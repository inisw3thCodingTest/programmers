# 230922_프로그래머스76501(음양 더하기)_조영조
def solution(absolutes, signs):
    answer=0
    for i in range(len(absolutes)):
        temp=int(absolutes[i])
        if signs[i] == True:
            answer+=temp
        else:
            answer-=temp
    return answer