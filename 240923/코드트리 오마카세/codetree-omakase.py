from collections import deque
import sys
input = sys.stdin.readline
L,Q = map(int,input().split())
Time=0
sushi_belt = deque([{} for _ in range(L)])
person = [[] for _ in range(L)]
total_sushi,total_person = 0,0

def remove_sushi(name,x):
    global sushi_belt,person,total_sushi,total_person
    while name in sushi_belt[x] and sushi_belt[x][name]>0:
        sushi_belt[x][name]-=1
        person[x][1]-=1
        total_sushi-=1

    if name in sushi_belt[x] and sushi_belt[x][name]==0:
        del sushi_belt[x][name]

    if person[x][1]==0:
        total_person-=1
        person[x]=[]

def rotate_table():
    global Time,sushi_belt
    Time+=1
    sushi_belt.rotate(1)
    for x in range(L):
        if len(person[x])!=0:
            # print("Time:{}".format(Time))
            remove_sushi(person[x][0],x)
    


while Q>0:
    rotate_table()
    quest = list(input().split())
    quest[0],quest[1] = map(int,quest[:2])
    if quest[1]!=Time:
        while quest[1]!=Time:
            rotate_table()
    if quest[0]==100:
        #quest[2]:x, quest[3]:name
        quest[2]=int(quest[2])
        if quest[3] in sushi_belt[quest[2]]:
            sushi_belt[quest[2]][quest[3]]+=1
        else: 
            sushi_belt[quest[2]][quest[3]]=1
        total_sushi+=1
        if len(person[quest[2]])!=0:
            remove_sushi(quest[3],quest[2])
        # print(sushi_belt)
    elif quest[0]==200:
        #quest[2]:x, quest[3]:name, quest[4]:n
        quest[2],quest[4]=int(quest[2]),int(quest[4])
        person[quest[2]]=[quest[3],quest[4]]
        total_person+=1
        remove_sushi(quest[3],quest[2])
    elif quest[0]==300:
        print(total_person,total_sushi)
    # print("Time:{},sushi_belt:{},person:{}".format(Time,sushi_belt,person))
    Q-=1