from collections import deque
R,C,K = map(int,input().split())
golem_list = [list(map(int,input().split())) for _ in range(K)]
answer = 0
R += 3
forest = [[0]*C for _ in range(R)]
forest_q = [[] for _ in range(K+1)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def check_range(r,c):
    return 0<=r<R and 0<=c<C


def check_direction(r,c,dr,dc):
    for ddr,ddc in zip(dr,dc):
        nr,nc = r+ddr,c+ddc
        if not(check_range(nr,nc)):
            return False
        if forest[nr][nc] != 0:
            return False
    return True

for i,(c,d) in enumerate(golem_list):
    r,c = 0,c-1
    br,bc = 0,0
    flag = False
    while True:
        if (check_direction(r+1,c,[0,1,0],[1,0,-1])):
            flag=True
            r,c = r+1,c 
        elif check_direction(r,c-1,[-1,1,0,1,2],[0,0,-1,-1,0]):
            flag=True
            r,c = r+1,c-1
            d = 3 if d-1<0 else d-1
        elif check_direction(r,c+1,[-1,0,1,2,1],[0,1,0,0,1]):
            flag=True
            r,c = r+1,c+1
            d = (d+1)%4
        if not flag :
            break
        flag = False

    if r<4:
        forest =[[0]*C for _ in range(R)]
        continue
    else:
        forest[r][c]=i+1
        for direct in range(4):
            nr,nc = r+dr[direct],c+dc[direct]
            forest[nr][nc]=i+1

    forest_q[i+1].append((r,c,d))
    q = deque()
    q.append((r,c,d))
    visited = [(r,c,d)]
    result = 0
    while q:
        now = q.popleft()
        exit = (now[0]+dr[now[2]],now[1]+dc[now[2]])
        result = max(now[0]+1-2,result)
        for direct in range(4):
            nr,nc = exit[0]+dr[direct],exit[1]+dc[direct]
            if not(check_range(nr,nc)):
                continue
            if forest[nr][nc]!=0 and forest[nr][nc]!=i+1 and forest_q[forest[nr][nc]] not in visited:
                q.append(forest_q[forest[nr][nc]][0])
                visited.append(forest_q[forest[nr][nc]])
    answer+=result
print(answer)