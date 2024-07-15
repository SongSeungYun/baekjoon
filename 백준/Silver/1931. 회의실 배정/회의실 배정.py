n=int(input())
cons=[]
for _ in range(n):
    cons.append(list(map(int,input().split(" "))))
cons.sort(key=lambda x : x[0])
cons.sort(key=lambda x : x[1])
end_time=cons[0][1]
answer=1
for i in range(1,n):
    if cons[i][0]>=end_time:
        answer+=1
        end_time=cons[i][1]
print(answer)