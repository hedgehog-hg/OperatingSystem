def solution(priorities, location):
    answer = 0
    max_p = max(priorities) 
    front = -1
    size = len(priorities)
    rear = size -1
    while True :
        front+=1
        front%=size
        if priorities[front] == max_p :
            answer +=1
            if front == location :
                break
            priorities[front]=0
            max_p = max(priorities)
        else :
            rear = front    
    return answer

# input data
priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities,location))
 