import sys
input=sys.stdin.readline
doku=[]
for i in range(9):
    doku.append(list(map(int,input().split(" "))))

def back(x,y):
    global doku
    if y==9:
        for i in range(9):
            print(" ".join(list(map(str,doku[i]))))
        exit(0)
    if doku[y][x]!=0:
        back((x+1)%9,y+(x+1)//9)
    if doku[y][x]==0:
        temp=[True]*10
        for i in range(9):
            temp[doku[y][i]]=False
            temp[doku[i][x]]=False
        for i in range(y-y%3,y-y%3+3):
            for j in range(x-x%3,x-x%3+3):
                temp[doku[i][j]]=False
        for i in range(1,10):
            if temp[i]:
                doku[y][x]=i
                back((x+1)%9,y+(x+1)//9)
                doku[y][x]=0

# def go_next(x,y):
#     global doku
#     if_nemo_good=False
#     temp=[1]*10
#     for i in range(y-y%3,y-y%3+3):
#         for j in range(x-x%3,x-x%3+3):
#             temp[doku[i][j]]-=1
#     for i in range(1,10):
#         if temp[i]!=0:
#             break
#     else:
#         if_nemo_good=True
#     if (x%3,y%3)==(2,2) and if_nemo_good:
#         return True
#     elif (x%3,y%3)!=(2,2):
#         return True
#     return False

back(0,0)