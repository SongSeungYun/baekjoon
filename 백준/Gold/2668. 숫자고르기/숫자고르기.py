n=int(input())
nums=[0]
for _ in range(n):
    nums.append(int(input()))

answer=[]
visited=[False]*(n+1)
def rec(l):
    global answer
    if len(l)!=1 and l[0]==l[-1]:
        answer+=l
        for i in l:
            visited[i]=True
        return
    
    next=nums[l[-1]]
    for j in range(1,len(l)):
        if l[j]==next:
            return
    else:
        rec(l+[next])

for i in range(1,n+1):
    if not visited[i]:
        rec([i])
answer=sorted(list(set(answer)))
print(len(answer))
for i in answer:
    print(i)