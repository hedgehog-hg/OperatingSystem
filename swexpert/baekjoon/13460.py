# 구슬 탈출 2
# n 세로x m 가로 보드 L R U D 기울이기 동작
# 빨간 구슬 빼기 -> success 
# 파란 구슬 빼기 -> failure
# 빨간 구슬 뺄 수 있는 최소 이동 값 출력

# input
n,m = map(int,input().split())
board = list()
for i in range(n) :
    board.append(list(map(str,input())))
    if 'R' in board[-1] : red = [i, board[-1].index('R')]
    if 'B' in board[-1] : blue = [i, board[-1].index('B')]

def move(x,y,dx,dy) :
    cnt = 0
    nx,ny = x,y
    while board[nx+dx][ny+dy] != '#' and board[nx][ny] != 'O' :
        nx += dx
        ny += dy
        cnt +=1
    return nx,ny,cnt

# solution
def solution() :
    visited = {}
    moves = [(-1,0),(1,0),(0,1),(0,-1)]
    visited[(red[0],red[1])] = 1
    stk = [[red[0],red[1],blue[0],blue[1],0]]

    while stk :
        rx,ry,bx,by,cnt = stk.pop(0)
        if cnt >= 10 : 
            return -1

        for dx,dy in moves :
            rrx, rry, rcnt = move(rx,ry,dx,dy)
            bbx, bby, bcnt = move(bx,by,dx,dy)

            if board[bbx][bby] != 'O' :
                if board[rrx][rry] == 'O' :
                    return cnt+1
                if rrx == bbx and rry == bby : # r,b가 같은 줄인 경우
                    if rcnt > bcnt :
                        rrx,rry = rrx-dx, rry-dy
                    else :
                        bbx,bby = bbx-dx,bby-dy
                if (rrx,rry,bbx,bby) in visited :
                    continue
                else:
                    visited[(rrx,rry,bbx,bby)] = 1
                    stk.append([rrx,rry,bbx,bby,cnt+1])
    return -1

print(solution())