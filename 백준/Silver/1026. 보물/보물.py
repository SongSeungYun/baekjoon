n=int(input())
a=sorted(list(map(int,input().split(" "))),reverse=True)
b=sorted(list(map(int,input().split(" "))))
answer=0
for i in range(n):
	answer+=a[i]*b[i]
print(answer)