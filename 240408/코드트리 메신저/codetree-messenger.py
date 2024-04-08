def say500(depth,node):
    global total
    for i in range(node, n+1):
        if data[i][0] == node and data[i][1] >= depth and data[i][2] == True:
            total +=1
            say500(depth+1,i)
n, q = map(int,input().split())
data = [[0,0,True] for i in range(n+1)]
for i in range(q):
    arr = list(map(int,input().split()))
    if i == 0: # 100
        for p in range(1,n+1):
            data[p][0] = arr[p]
        for a in range(n+1,len(arr)):
            data[a-n][1] = arr[a]
        # print(data)

    if arr[0] == 500:
        total = 0
        say500(1,arr[1])
        print(total)

    elif arr[0] == 300:
        data[arr[1]][1] = arr[2]
    
    elif arr[0] == 200:
        data[arr[1]][2] = not data[arr[1]][2]
    
    elif arr[0] == 400:
        temp = data[arr[1]][0]
        data[arr[1]][0] = data[arr[2]][0]
        data[arr[2]][0] = temp