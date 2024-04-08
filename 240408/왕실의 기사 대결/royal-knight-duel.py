def rect_pos(idx,r,c,h,w):
    global pos, gisa
    for i in range(r,r+h):
        for j in range(c,c+w):
            pos[idx].append((i-1,j-1))
            gisa[i-1][j-1] = idx

def is_inrange(x,y):
    return x>=0 and x<l and y>=0 and y<l

def move(idx,d):
    global pos, is_live,answer
    new_pos = []
    prev_nr,prev_nc =-1,-1
    for r,c in pos[idx]:
        nr = r+dr[d]
        nc = c+dc[d]
        new_pos.append((nr,nc))
        # print("nr,nc",nr,nc)

        if prev_nr!=r and prev_nc!=c:
            gisa[r][c] = 0
        gisa[nr][nc] = idx
        # print("fisrt_idx:",fisrt_idx,"idx:",idx)
        if idx != fisrt_idx:
            if board[nr][nc]==1:
                # print("board[nr][nr]==1 ,nr,nc",nr,nc)
                power[idx]-=1
            if power[idx]==0:
                is_live[idx]=False
        # print("power:",power)
        # print("is_live:",is_live)
        
        prev_nr,prev_nc = nr,nc
    pos[idx] = new_pos 


def dfs(idx,d):
    global  canGo
    if not canGo:
        return
    for r,c in pos[idx]:
        nr = r+dr[d]
        nc = c+dc[d]
        # print("r,c:",r,c,"nr,nc:",nr,nc)
        if not(is_inrange(nr,nc) and board[nr][nc]!=2):
            # print("cnaGo Flase - nr,nc:",nr,nc)
            canGo = False
            return
        if gisa[nr][nc]>0 and gisa[nr][nc]!=idx:
            dfs(gisa[nr][nc],d)
            if canGo:
                # print("cnaGo True ",gisa[nr][nc],nr,nc)
                move(gisa[nr][nc],d)
    return

def print_data(arr):
    for i in range(l):
        print(arr[i])



l,q,n = map(int,input().split())

pos = [[] for _ in range(n+1)]
gisa = [[0]*l for _ in range(l)]
is_live = [True]*(n+1)
origin_power = [0]*(n+1)
power = []
dr = [-1,0,1,0]
dc = [0,1,0,-1]

board =[list(map(int,input().split())) for _ in range(l)]

for i in range(n):
    r,c,h,w,k = map(int,input().split())
    rect_pos(i+1,r,c,h,w)
    origin_power[i+1] = k
power = origin_power.copy()


for i in range(1,q+1):
    # print("----board-------")
    # print_data(board)
    # print("----gisa-------")
    # print_data(gisa)
    # print(i,"번째 명령")
    idx, d = map(int,input().split())
    fisrt_idx = idx
    if not is_live[idx]:
        continue
    canGo = True
    dfs(idx,d)
    if canGo:
        move(idx,d)
origin_sum = 0
last_sum = 0
for i in range(1,n+1):
    if is_live[i]:
        last_sum +=power[i]
        origin_sum +=origin_power[i]

print(origin_sum - last_sum)