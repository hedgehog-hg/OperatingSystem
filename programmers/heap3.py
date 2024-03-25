import heapq
def solution(operations) :
    max_heap = []
    min_heap = []
    for operation in operations :
        if operation == 'D 1' and max_heap:
            heapq.heappop(max_heap)
            if not max_heap :
                max_heap = []
                min_heap = []
        elif operation == 'D -1' and min_heap:
            heapq.heappop(min_heap)
            if not min_heap :
                max_heap = []
                min_heap = []
        else :
            n = int(operation.split()[1])
            heapq.heappush(max_heap,-n)
            heapq.heappush(min_heap,n)
    if not min_heap:
        return [0,0]
    heap = []
    for n in max_heap :
        heap.append(-n)
    heap = list(set(heap)&set(min_heap)) # intersection -> 삭제 되지 않은 원소임을 보장

    return [max(heap),min(heap)]

#input data
operations =["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))
