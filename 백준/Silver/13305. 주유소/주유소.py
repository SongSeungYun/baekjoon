n=int(input())
cost=list(map(int,input().split(" ")))
city=list(map(int,input().split(" ")))
answer=0
min_city=city[0]
for i in range(n-1):
    if city[i]<min_city:
        min_city=city[i]
    answer+=min_city*cost[i]
print(answer)