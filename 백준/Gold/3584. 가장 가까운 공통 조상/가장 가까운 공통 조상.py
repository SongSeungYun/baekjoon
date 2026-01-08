import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    #tree=[[] for __ in range(n)]
    child_parent={}
    for __ in range(n-1):
        v1,v2=map(int,input().split(" "))
        child_parent[v2]=v1
    a,b=map(int,input().split(" "))
    visited=[False for i in range(n+1)]
    try:
        while True:
            visited[a]=True
            a=child_parent[a]
    except:
        pass

    try:
        while not visited[b]:
            # print("진행중:",b)
            visited[b]=True
            b=child_parent[b]
    except:
        pass
    print(b)
    # for i in range(-1,-min(len(a_ancestor),min(b_ancestor))-1,-1):
    #     if a_ancestor[i]!=b_ancestor[i]:
    #         print(a_ancestor[i+1])
    #         break
    # else:
    #     if len(a_ancestor)>len(b_ancestor):
    #         print(b_ancestor[0])
    #     else:
    #         print(a_ancestor[0])