def rec(x,y,num):
    if num==1:
        return
    for i in range(y+num//3,y+2*num//3):
        for j in range(x+num//3,x+2*num//3):
            answer_list[i][j]=" "
    for i in range(3):
        for j in range(3):
            rec(x+j*num//3,y+i*num//3,num//3)
n=int(input())
answer_list=[["*"]*n for _ in range(n)]
rec(0,0,n)
for i in answer_list:
    print("".join(i))