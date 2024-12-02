import sys
import itertools
input=sys.stdin.readline
n,m=map(int,input().split(" "))
cities=[list(map(int,input().split(" "))) for _ in range(n)]
houses=[]
bbqs=[]

for i in range(n):
    for j in range(n):
        if cities[i][j]==1:
            houses.append((i,j))
        elif cities[i][j]==2:
            bbqs.append((i,j))

answer=100*100*13+1
for bbq in itertools.combinations(bbqs,m):
    distance=0
    for house in houses:
        distance+=min([abs(house[0]-bb[0])+abs(house[1]-bb[1]) for bb in bbq])
    answer=min(answer,distance)
print(answer)