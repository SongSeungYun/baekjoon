import sys
input = lambda: sys.stdin.readline().strip()
n,m=map(int,input().split(" "))
name_to_id={}
names=[]
cur_index=0
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=input().split(" ")
    if a not in name_to_id:
        name_to_id[a]=cur_index
        names.append(a)
        cur_index+=1
    if b not in name_to_id:
        name_to_id[b]=cur_index
        names.append(b)
        cur_index+=1
    graph[name_to_id[a]].append(name_to_id[b])#a가 b보다 늙음
# print(graph)
# print(name_to_id)
q=int(input())
for i in range(q):
    start_nodes=input().split(" ")
    answer="gg"
    if_find=False
    if start_nodes[0] not in name_to_id or start_nodes[1] not in name_to_id or start_nodes[0]==start_nodes[1]:
        print(answer, end=" ")
        continue

    #print(start_nodes)
    for i in range(2):
        start_nodes[i]=name_to_id[start_nodes[i]]
    for start in start_nodes:
        #print("이번 시작은 ",start)
        end=sum(start_nodes)-start
        stack=[start]
        visited=[False for i in range(n)]
        while stack:
            cur=stack.pop()
            visited[cur]=True
            #print("컬 스타트 엔드 스택:",cur,start,end,stack)
            if cur==end:#정답 체크
                if_find=True
                answer=start
                #print("정답체크함")
                break
            for i in graph[cur]:
                if not visited[i]:
                    stack.append(i)
        if if_find:
            break
    if answer=="gg":
        print("gg ",end="")
    else:
        print(names[answer]," ",sep="",end="")
    #print()