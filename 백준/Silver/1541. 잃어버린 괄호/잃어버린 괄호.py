s=input()
num=[]
answer=0
l=len(s)
i=0
last_num="+"
while True:
    if i==l:
        break
    elif s[i]=="-":
        answer+=int("".join(num))
        num=[]
        last_num="-"
        break
    elif s[i]=="+":
        answer+=int("".join(num))
        num=[]
    else:
        num.append(s[i])
    i+=1

for j in range(i+1,l):
    if s[j]=="+" or s[j]=="-":
        answer-=int("".join(num))
        num=[]
    else:
        num.append(s[j])
if last_num=="+":
    answer+=int("".join(num))
else:
    answer-=int("".join(num))
print(answer)