def solution(arr):
    """
    연속된 숫자가 나오지 않게 하기 위해서,
    이전에 나온 숫자를 저장해두고, 이를 비교해서 넣는다.
    """
    answer = []
    last = -1
    for v in arr:
        if v != last:
            answer.append(v)
        last = v
    return answer