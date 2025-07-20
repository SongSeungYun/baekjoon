max_sosu=1000002
if_sosu=[True]*max_sosu#2~1000001
for i in range(2,max_sosu):
    if if_sosu[i-2]:
        for j in range(2*i,max_sosu,i):
            if_sosu[j]=False
#print(if_sosu)

n,m=map(int,input().split(" "))
if_jegopsu=[False for _ in range(m-n+1)]
for i in range(2,max_sosu):
    if not if_sosu[i]:
        continue
    ii=i*i
    start=((n+ii-1)//ii)*ii
    for num in range(start,m+1,ii):
        if_jegopsu[num-n]=True
print(if_jegopsu.count(False))