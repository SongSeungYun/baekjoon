n=int(input())
maps=[]
for i in range(n):
    maps.append(list(map(int,input().split(" "))))
answer=100*400+1
def other_score(team):
    temp=[i for i in range(n+1)]
    temp_answer=0
    for i in team:
        temp[i]=0
    for i in range(1,n+1):
        if temp[i]:
            for j in range(i+1,n+1):
                if temp[j]:
                    temp_answer+=maps[i-1][j-1]+maps[j-1][i-1]
    return temp_answer
def back(team,team_num,score):
    global answer
    if team_num==n//2:
        answer=min(abs(other_score(team)-score),answer)
        return
    for i in range(team[-1]+1,n//2+team_num+2):
        back(team+[i],team_num+1,score+sum((maps[i-1][k-1]+maps[k-1][i-1]) for k in team))
for i in range(2,n//2+3):
    back([1,i],2,maps[0][i-1]+maps[i-1][0])
print(answer)