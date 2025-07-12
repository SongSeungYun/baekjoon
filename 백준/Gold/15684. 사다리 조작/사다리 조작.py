import sys
input=lambda:sys.stdin.readline().strip()
n,m,h=map(int,input().split(" "))
garosuns=[[False]*(n+1) for _ in range(h+1)]
for _ in range(m):
    a,b=map(int,input().split(" "))
    garosuns[a][b]=True

def is_answer():
    global garosuns
    for start_i in range(1,n+1):
        cur_i=start_i
        for j in range(1,h+1):
            if garosuns[j][cur_i-1]:
                cur_i-=1
            elif garosuns[j][cur_i]:
                cur_i+=1
        if cur_i!=start_i:
            return False
    return True

def rec(x,y,add_garosun):
    global answer,garosuns
    if x>n:#좌표 갱신
        x=1
        y+=1
    #print(x,y,add_garosun)
    if add_garosun>=answer:#정답 확인 전 가지치기
        return
    if is_answer():#정답 확인
        answer=min(answer,add_garosun)
        return
    if add_garosun==3:#정답 확인 후 가지치기
        return
    if y>h:#정답 확인,좌표 갱신 후 가지치기
        return
    for i in range(y,h+1):
        start_j=x if i==y else 1
        for j in range(start_j,n):
            if not any(garosuns[i][j-1:j+1]):
                #rec(x+1,y,add_garosun)
                garosuns[i][j]=True
                rec(x+2,y,add_garosun+1)
                garosuns[i][j]=False
answer=4
rec(1,1,0)
print(-1 if answer==4 else answer)