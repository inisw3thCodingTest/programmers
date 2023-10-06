def solution(numbers):
    answer = 0

    # 1. 0-9까지는 무조건 있기 때문에 모범답안 설정
    good_answer = [0,1,2,3,4,5,6,7,8,9]

    # 2. 만약, 있어야 하는 숫자가 없을 경우에, 없는 숫자를 더해준다.
    for num in good_answer:
        if num not in numbers:
            answer += num

    return answer
