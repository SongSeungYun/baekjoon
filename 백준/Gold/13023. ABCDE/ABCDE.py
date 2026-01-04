import sys
input=sys.stdin.readline

n,m=map(int, input().split())
g =[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited=[False]*n
ans=0

def dfs(v, depth):
    global ans
    if ans:
        return
    if depth==4:
        ans=1
        return

    for nx in g[v]:
        if not visited[nx]:
            visited[nx]=True
            dfs(nx,depth+1)
            visited[nx]=False

for s in range(n):
    visited[s]=True
    dfs(s,0)
    visited[s]=False
    if ans:
        break

print(ans)
