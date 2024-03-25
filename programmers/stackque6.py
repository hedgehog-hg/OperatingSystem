def solution(prices):
    answer = [0] * len(prices)
    stk =[0]
    size = len(prices) -1
    for i in range(1,size) :
        while stk and prices[i] < prices[stk[-1]] :
            index = stk.pop()
            answer[index] = i - index
        stk.append(i)
    while stk :
        index = stk.pop()
        answer[index] = size - index
    return answer

# 가격 상승 구간 / 하락 구간으로 구분
# 가격 상승 구간을 stk에 저장
# prices[i] < prices [stk[-1]] 하락 구간에 진입했을 때
# 해당 시점으로부터 역으로 계산
# e.g prices[3] 일 때 index 2,1,0 계산해서 index에 저장
# 마지막 while은 상승 구간으로 끝나서 남은 값 계산

# input data
prices = [1,2,3,2,3]
print(solution(prices))

