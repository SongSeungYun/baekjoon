from collections import deque
def bfs(N,graph,root):
  graph=graph
  visited=[1]+[0]*N
  q=deque([root])
  answer=[0]*(N+1)
  cnt=1
  while q:
    node=q.popleft()
    if visited[node]:
      continue
    visited[node]=1
    answer[node]=cnt
    cnt+=1
    for i in graph[node]:
      if not visited[i]:
        q.append(i)
  return answer
N,M,R=map(int,input().split(" "))
graph=[[] for _ in range(N+1)]
for i in range(M):
  u,v=map(int,input().split(" "))
  graph[u].append(v)
  graph[v].append(u)
for i in range(1,N+1):
  graph[i].sort()
answer=bfs(N,graph,R)
for i in range(1,N+1):
  print(answer[i],sep="\n")