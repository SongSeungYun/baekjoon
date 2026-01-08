# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def get_root(node):
#     try:
#         while True:
#             node=child_parent[node]
#     except:
#         return node

# def get_max(node):
#     global answer
#     #print("노드:",node)
#     if node not in parent_child:
#         return (0,0)
    
#     max1,max2=0,0
#     for i in parent_child[node]:
#         cur_value=vertexes[(node,i)]+max(get_max(i))
#         if max1<cur_value:
#             max2=max1
#             max1=cur_value
#         elif max2<cur_value:
#             max2=cur_value
#     answer[node]=max1+max2
#     return (max1,max2)
# n=int(input())
# child_parent={}
# parent_child={}
# vertexes={}
# for _ in range(n-1):
#     a,b,cost=map(int,input().split(" "))
#     vertexes[(a,b)]=cost
#     child_parent[b]=a
#     if a in parent_child:
#         parent_child[a].append(b)
#     else:
#         parent_child[a]=[b]
# # print(root)
# # for ii in range(1,n+1):
# #     print(ii,get_max(ii))
# # print(answer)
# answer=[0]*(n+1)
# get_max(get_root(1))
# print(max(answer))
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_root(node):
    try:
        while True:
            node=child_parent[node]
    except:
        return node

def get_max(node):
    global answer
    #print("노드:",node)
    if node not in parent_child:
        return (0,0)
    
    max1,max2=0,0
    for i in parent_child[node]:
        cur_value=vertexes[(node,i)]+max(get_max(i))
        if max1<cur_value:
            max2=max1
            max1=cur_value
        elif max2<cur_value:
            max2=cur_value
    answer=max(answer,max1+max2)
    return (max1,max2)
n=int(input())
child_parent={}
parent_child={}
vertexes={}
for _ in range(n-1):
    a,b,cost=map(int,input().split(" "))
    vertexes[(a,b)]=cost
    child_parent[b]=a
    if a in parent_child:
        parent_child[a].append(b)
    else:
        parent_child[a]=[b]
# print(root)
# for ii in range(1,n+1):
#     print(ii,get_max(ii))
# print(answer)
answer=0
get_max(get_root(1))
print(answer)