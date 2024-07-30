import sys
n,m=map(int,sys.stdin.readline().split(" "))
graph={i:[] for i in range(1,n+1)}
l=list(map(int,sys.stdin.readline().split(" ")))
for i in range(1,n):
    graph[l[i]].append(i+1)

first_chingchan=[0]*(n+1)
dp=[0]*(n+1)
for _ in range(m):
    i,w=map(int,sys.stdin.readline().split(" "))
    first_chingchan[i]+=w
stack=[1]
while stack:
    now=stack.pop()
    for j in graph[now]:
        dp[j]+=dp[now]+first_chingchan[j]
        stack.append(j)
print(" ".join(map(str,dp[1:])))