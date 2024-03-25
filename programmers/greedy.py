def solution(n, lost, reserve):
    # reserve +- 1 == lost 일 때 빌려 줄 수 있음
    # 체육 수업을 들을 수 있는 최대 학생 수 구하기
    # 2 <= n <= 30
    cnt = 0 # 수업 못 듣는 학생
    inter = set(lost)&set(reserve)
    lost = list(set(lost).difference(inter))
    reserve = list(set(reserve).difference(inter))
    for student in lost :
        print(student)
        if (student-1) in reserve :
            print(1)
            reserve.remove(student-1)
        elif (student+1) in reserve :
            print(2)
            reserve.remove(student+1)
        else :
            print('?')
            cnt +=1
    print(cnt)
    return n - cnt

print(solution(5,[4,5],[3,4]))