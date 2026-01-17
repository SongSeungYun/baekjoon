import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
import math

n,b=map(int,input().split(" "))
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split(" "))))

for i in range(n):
    for j in range(n):
        mat[i][j]%=1000
    
def mul_mat(m1,m2):
    temp_mat=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp_mat[i][j]=(temp_mat[i][j]+m1[i][k]*m2[k][j])%1000
    return temp_mat
    
def rec(time):
    if time==1:
        return mat

    temp_mat=rec(time//2)
    if time%2==0:
        return mul_mat(temp_mat,temp_mat)
    else:
        return mul_mat(mul_mat(temp_mat,temp_mat),mat)

answer=rec(b)
for i in answer:
    for j in i:
        print(j,end=" ")
    print()