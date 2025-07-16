import sys
input=lambda:sys.stdin.readline().strip()
t=int(input())
for _ in range(t):
    n=int(input())
    choice=[0]+list(map(int,input().split(" ")))
    visited=[False]*(n+1)
    answer=n
    for i in range(1,n+1):
        if visited[i]:
            continue
        #print("아이 :",i)
        cur_student=i
        member=[]
        while True:
            if visited[cur_student]:
                for i in range(len(member)):
                    if member[i]==cur_student:
                        answer-=len(member)-i
                        #print("맴버 숫자 :",len(member)-i)
                break
            #print("현재 학생 :",cur_student)
            visited[cur_student]=True
            member.append(cur_student)
            cur_student=choice[cur_student]
    print(answer)