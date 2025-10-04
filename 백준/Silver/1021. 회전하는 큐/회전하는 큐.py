from collections import deque
n,m=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))
q=deque([i for i in range(1,n+1)])
answer=0
for i,num in enumerate(nums):
    rotate_num=0
    while q[0]!=num:
        q.append(q.popleft())
        rotate_num+=1
    q.popleft()
    answer+=min(rotate_num,n-i-rotate_num)
print(answer)