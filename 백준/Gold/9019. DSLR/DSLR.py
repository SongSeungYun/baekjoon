def convert(n,c):
  if c=="D":
    return (2*n)%10000
  elif c=="S":
    return (n-1)%10000
  elif c=="L":
    return (n%1000)*10+n//1000
  else:
    return (n%10)*1000+n//10
    
from collections import deque

t=int(input())
command=["D","S","L","R"]
for _ in range(t):
  visited=[0 for i in range(10000)]
  a,b=map(int,input().split(" "))
  visited[a]=1
  q=deque([(a,"")])
  while q:
    num,c=q.popleft()
    if num==b:
      print(c)
      break
    for nc in command:
      result=convert(num,nc)
      if not visited[result]:
        visited[result]=1
        q.append((result,c+nc))