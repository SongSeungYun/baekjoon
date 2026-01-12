from collections import deque

n,k=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))
answer=sorted(nums)

visited={}
def make_permutation(l):
    global visited
    if len(l)==n:
        visited[tuple(l)]=False
        return
    for i in range(1,n+1):
        if i not in l:
            make_permutation(l+[i])
make_permutation([])

q=deque()
q.append((nums,0))
visited[tuple(nums)]=True
if_answer=False
while q:
    cur_list,time=q.popleft()
    if cur_list==answer:
        if_answer=True
        print(time)
        break
    for i in range(n-k+1):
        temp_list=[]
        for j in range(i):
            temp_list.append(cur_list[j])
        for j in range(i+k-1,i-1,-1):
            temp_list.append(cur_list[j])
        for j in range(i+k,n):
            temp_list.append(cur_list[j])
        if not visited[tuple(temp_list)]:
            visited[tuple(temp_list)]=True
            q.append((temp_list,time+1))
if not if_answer:
    print(-1)