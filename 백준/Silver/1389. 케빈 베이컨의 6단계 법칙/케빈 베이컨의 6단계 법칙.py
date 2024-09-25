import sys
from copy import deepcopy
input=sys.stdin.readline
n,m=map(int,input().split(" "))
INF=int(1e9)
graph=[[INF]*n for _ in range(n)]
for i in range(n):
    graph[i][i]=0
for _ in range(m):
    a,b=map(int,input().split(" "))
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b], graph[a][k] + graph[k][b])
bacon=[sum(i) for i in graph]
print(bacon.index(min(bacon))+1)