a,b,c=map(int,input().split(" "))
bb=int(b**0.5)
num=a**bb%c
answer=1
for i in range(bb):
    answer*=num
    answer%=c
answer*=a**(b-bb**2)
answer%=c
print(answer)