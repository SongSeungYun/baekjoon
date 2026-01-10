n=int(input())
emsu,yangsu=[],[]
answer=0
for _ in range(n):
    temp=int(input())
    if temp==1:
        answer+=1
    elif temp<=0:
        emsu.append(temp)
    else:
        yangsu.append(temp)
emsu.sort()
yangsu.sort(reverse=True)
for i in range(0,len(yangsu),2):
    if i+1==len(yangsu):
        answer+=yangsu[i]
    else:
        answer+=yangsu[i]*yangsu[i+1]

for i in range(0,len(emsu),2):
    if i+1==len(emsu):
        answer+=emsu[i]
    else:
        answer+=emsu[i]*emsu[i+1]

print(answer)

    


'''
기본 규칙: 음수 2개씩 양수 2개씩(절대값 큰 애들 순서대로)

1-1)음수 짝수 0 양수 짝수
1-2)음수 짝수 양수 짝수

2-1)음수 홀수 0 양수 짝수
2-2)음수 홀수 양수 짝수 -> 절대값 가장 작은 음수 더하기

3-1)음수 홀수 0 양수 홀수 -> 가장 작은 양수 더하기
3-2)음수 홀수 양수 홀수 -> 남는 두 개 묶을때, 안묶을 때 비교해서 선택

4-1)음수 짝수 0 양수 홀수 -> 절대값 가장 작은 양수 더하기
4-2)음수 짝수 양수 홀수 -> 절대값 가장 작은 양수 더하기
'''