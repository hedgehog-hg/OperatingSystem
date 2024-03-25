import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True :
        f = heapq.heappop(scoville)
        if f >= K : return answer
        heapq.heappush(scoville,f + heapq.heappop(scoville)*2)
        answer +=1
    return -1

#input data
s = [1, 2, 3, 9, 10, 12]
print(solution(s,7))