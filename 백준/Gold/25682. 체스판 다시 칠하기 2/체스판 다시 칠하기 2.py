import sys
n,m,k=map(int,sys.stdin.readline().split(" "))
board=[]
hol={"B":1,"W":0}
jjak={"B":0,"W":1}
answer=k*k
for _ in range(n):
    board.append(sys.stdin.readline())
sums=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    if (i+1)%2==0:
        sums[i][1]=sums[i-1][1]+jjak[board[i-1][0]]
    else:
        sums[i][1]=sums[i-1][1]+hol[board[i-1][0]]

for i in range(n):#행+열이 짝수->w +1 홀수->b +1
    for j in range(1,m):
        if (i+j)%2==0:
            sums[i+1][j+1]=sums[i][j+1]+sums[i+1][j]-sums[i][j]+jjak[board[i][j]]
        else:
            sums[i+1][j+1]=sums[i][j+1]+sums[i+1][j]-sums[i][j]+hol[board[i][j]]

for i in range(k,n+1):
    for j in range(k,m+1):
        temp=sums[i][j]-sums[i-k][j]-sums[i][j-k]+sums[i-k][j-k]
        answer=min(answer,min(temp,k*k-temp))
print(answer)