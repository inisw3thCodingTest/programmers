def solution(s):
    num_li = s.split(" ")  # 1. 리스트 형태로 저장.

    # 2. 최대값 최소값 설정
    min = 99999
    max = -99999

    for num in num_li:
        num = int(num) # 숫자형태로 바꿔준다.
        # 3. 수 각각 비교해서, 최대값 최소값을 대체
        if num < min:
            min = num
        if num > max:
            max = num

    answer = f"{min} {max}"  # 4. str 형태로 바꿔준다.
    return answer
