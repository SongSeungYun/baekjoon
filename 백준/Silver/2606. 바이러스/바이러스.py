n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
  u,v=map(int,input().split(" "))
  graph[u].append(v)
  graph[v].append(u)
for i in range(1,n+1):
  graph[i].sort()
visited=[0]*(n+1)
answer=0
root=1
stack=[root]
while stack:
  node=stack.pop()
  if visited[node]:
    continue
  visited[node]=1
  answer+=1
  for add_node in graph[node]:
    if not visited[add_node]:
      stack.append(add_node)
print(answer-1)