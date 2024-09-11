from heapq import heappop,heappush
# from collections import deque
Q =int(input())
start = 0
INF = int(1e9)
G = []
I = []
dic = {}
def dijkstra(start):
    q = []
    init_w = 0
    heappush(q,(init_w,start))
    distance=[INF]*n
    distance[start]=init_w
    while q:
        cost,v = heappop(q)
        if distance[v]<cost:
            continue
        for nv,nw in G[v]:
            ncost = cost+nw
            if ncost < distance[nv]:
                distance[nv]=ncost
                heappush(q,(ncost,nv))
    return distance
for q_idx in range(Q):
    orders = list(map(int,input().split()))
    # print("q_idx:{} orders:{}".format(q_idx,orders))
    if orders[0]==100:
        n,m = orders[1],orders[2]
        G = [[] for _ in range(n)]
        for i in range(1,m+1):
            v,u,w = orders[i*3:i*3+3]
            G[v].append((u,w))
            G[u].append((v,w))

    elif orders[0]==200:
        id,revenue,dest = orders[1],orders[2],orders[3]
        if start not in dic:
            dic[start] = dijkstra(start)
        # print("dic[{}]:{}".format(start,dic[start]))
        # print("dest:{},cost:{}".format(dest,dic[start][dest]))
        cost = dic[start][dest]
        heappush(I,(-(revenue-cost),id,revenue,dest))
        # print("q_idx:{} 200 heappush heap  :{}".format(q_idx,I))

    elif orders[0]==300:
        id = orders[1]
        temp = []
        while I:
            minus_profit,idx,revenue,dest = heappop(I)
            if idx == id:
                break
            else:
                temp.append((minus_profit,idx,revenue,dest))
        for item in temp:
            heappush(I,item)
        # print("q_idx:{} 300 heappop heap  :{}".format(q_idx,I))

    elif orders[0]==400:
        if I:
            minus_profit,idx,revenue,dest = heappop(I)
            if minus_profit>0:
                # print("q_idx:{} answer:{}".format(q_idx,-1))
                # print("answer:{}".format(-1))
                print(-1)
                heappush(I,(minus_profit,idx,revenue,dest))
            else:
                # print("answer:{}".format(idx))
                print(idx)
                # print("q_idx:{} answer:{}".format(q_idx,idx))
                    
        else:
            # print("answer:{}".format(-1))
            print(-1)
        #     print("no I")
        # print("q_idx:{} 400 heappop heap  :{}".format(q_idx,I))


    elif orders[0]==500:
        start = orders[1]
        dic[start] = dijkstra(start)
        temp = []
        while I:
            minus_profit, idx,revenue,dest = heappop(I)
            cost = dic[start][dest]
            temp.append((-(revenue-cost),idx,revenue,dest))  
        for item in temp:
            heappush(I,item)
        # print("q_idx:{} 500 heappush heap  :{}".format(q_idx,I))