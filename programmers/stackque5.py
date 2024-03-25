def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = [0] * bridge_length
    while que :
        answer+=1
        que.pop(0)
        if truck_weights :
            if sum(que) + truck_weights[0] <= weight :
                que.append(truck_weights.pop(0))
            else :
                que.append(0)
    return answer

# input data
bridge_length = 100 # 최대 올라갈 수 있는 대수
weight = 100 # 견딜수 있는 무게
truck_weights = [10] # 트럭 무게
print(solution(bridge_length,weight,truck_weights))

