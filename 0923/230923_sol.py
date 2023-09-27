# 230923토_프로그래머스140108(문자열 나누기)_조영조
def solution(s):
    answer = 0
    
    #문자열 첫글자 세팅
    temp_char=s[0]
    cnt_left=1
    cnt_right=0

    for i in range(1,len(s)-1):#두번째부터 마지막 하나 앞까지
        if cnt_left==0:#조건만족하고 끊어지면 다시 세팅
            temp_char=s[i]
            cnt_left=1
            cnt_right=0
        else:
            if s[i]==temp_char:
                cnt_left+=1
            else:
                cnt_right+=1
                if cnt_left==cnt_right:#조건만족하면끊은횟수+1
                    answer+=1
                    cnt_left=0
                    cnt_right=0

    answer+=1#만들어진 개수는 끊은 횟수+1
    return answer