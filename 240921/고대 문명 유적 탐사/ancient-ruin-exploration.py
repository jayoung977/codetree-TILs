from heapq import heappush, heappop
from collections import deque
import copy
K,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(5)]
ujuk = list(map(int,input().split()))
ujuk = deque([u for u in ujuk])
# print("ujuk:{}".format(ujuk))
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def rotate(data):
    rotated = [[0]*len(data) for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            rotated[j][len(data)-1-i]=data[i][j]
    return rotated

def filltodata(r,c):
    data = [[0]*3 for _ in range(3)]
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            data[i-r+1][j-c+1]=graph[i][j]
    return data

def filltograph(test_graph,rotated,r,c):
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            test_graph[i][j]=rotated[i-r+1][j-c+1]
    return test_graph


def dfs(r,c,visited,test_graph,path):
    for d in range(4):
        nr,nc = r+dr[d],c+dc[d]
        if not(0<=nr<5 and 0<=nc<5):
            continue
        if visited[nr][nc]==1:
            continue
        if test_graph[nr][nc]!=test_graph[r][c]:
            continue
        visited[nr][nc]=1
        path.append((nr,nc))
        dfs(nr,nc,visited,test_graph,path)


def get_ujuk(test_graph):
    # print("test_graph")
    # for row in test_graph:
    #     print(row)
    visited = [[0]*5 for _ in range(5)]
    result= 0
    path_list = []
    for r in range(5):
        for c in range(5):
            if visited[r][c]!=1:
                path = [(r,c)]
                visited[r][c]=1
                dfs(r,c,visited,test_graph,path)
                # print("r:{},c:{},path:{}".format(r,c,path))
                if len(path)>=3:
                    result+=len(path)
                    path_list+=path

    return (result, path_list)

def insert_new_ujuk(path_list,ujuk,f_test_graph):
    path_hq = []
    # print("path_list:{}".format(path_list))
    for p_r,p_c in path_list:
        heappush(path_hq,(p_c,-1*p_r))
    # print("path_hq:{}".format(path_hq))
    # while path_hq and ujuk:
    while path_hq :
        p_c,p_r = heappop(path_hq)
        p_r = -1*p_r
        f_test_graph[p_r][p_c]=ujuk.popleft()

    # print("def_new_f_test_graph")
    # for row in f_test_graph:
    #     print(row)

    return f_test_graph


while K>0:
    hq=[]
    for i in range(1,4):
        for j in range(1,4):
            rotated = filltodata(i,j)
            for k in range(3):
                rotated = rotate(rotated)
                # print("rotate")
                # for row in rotated:
                #     print(row)
                test_graph = copy.deepcopy(graph)
                test_graph = filltograph(test_graph,rotated,i,j)
                result, path_list = get_ujuk(test_graph)
                # print("i:{},j:{},k:{},result:{},path_list:{}".format(i,j,k,result,path_list))
                heappush(hq,(-1*result,k,j,i,path_list,test_graph))
    # print("hq:{}".format(hq))
    f_result,f_k,f_j,f_i,f_path_list,f_test_graph = heappop(hq)
    f_result = -1*f_result
    # print("f_test_graph")
    # for row in f_test_graph:
    #     print(row)
    # print("f_result:{},f_k:{},f_j:{},f_i:{},f_path_list:{}".format(f_result,f_k,f_j,f_i,f_path_list))
    if f_result == 0:
        break
    
    f_test_graph = insert_new_ujuk(f_path_list,ujuk,f_test_graph)
    # print("new_f_test_graph")
    # for row in f_test_graph:
    #     print(row)


    while True:
        result, path_list = get_ujuk(f_test_graph)
        # print("result:{}, path_list:{}".format(result, path_list))
        if result == 0:
            break
        else:
            f_result+=result
            f_test_graph = insert_new_ujuk(path_list,ujuk,f_test_graph)
            # print("new_f_test_graph")
            # for row in f_test_graph:
            #     print(row)
    graph = f_test_graph
    print(f_result, end = " ")


    K-=1