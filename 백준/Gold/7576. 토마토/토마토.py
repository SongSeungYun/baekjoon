from collections import deque
import sys

q = deque()
target=0
how_many_one=0
m, n = map(int, input().split(" "))
box = []

for i in range(n):
  temp = list(map(int, sys.stdin.readline().split()))
  for j in range(m):
    if temp[j] == 1:
      how_many_one+=1
      target+=1
      q.append([j, i,0])
    elif temp[j] == 0:
      target+= 1
  box.append(temp)
  
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
while q:
  x,y,day=q.popleft()
  for i in range(4):
    now_x = x + dx[i]
    now_y = y + dy[i]
    if 0<=now_x<m and 0<=now_y<n and box[now_y][now_x] == 0:
      box[now_y][now_x]=1
      how_many_one+=1
      q.append([now_x,now_y,day+1])
if how_many_one==target:
  print(day)
else:
  print(-1)