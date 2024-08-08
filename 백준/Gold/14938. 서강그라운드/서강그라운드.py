n,m,r=map(int,input().split(" "))
t=list(map(int,input().split(" ")))
graph=[[16]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,l=map(int,input().split(" "))
    graph[a][b]=l
    graph[b][a]=l
for i in range(1,n+1):
    graph[i][i]=0
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])
answer=0
for i in range(1,n+1):
    temp_answer=0
    for j in range(1,n+1):
        if graph[i][j]<=m:
            temp_answer+=t[j-1]
    answer=max(answer,temp_answer)
print(answer)