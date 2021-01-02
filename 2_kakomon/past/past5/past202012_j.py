from collections import deque
s=input()
x=int(input())
coms=[]
curr=''
for si in s:
    if '1'<=si<='9':
        coms.append(('n',int(si)))
    else:
        coms.append(('s',si))

# print(coms)
cnt=0
q=deque()
for com,val in coms:
    if com=='s':
        cnt+=1
        q.append((com,val,cnt))
        if cnt>=x:
            print(val)
            exit()
    else:
        cnt*=(val+1)
        q.append((com,val,cnt))
        if cnt>=x:break

while q:
    com,val,c_cnt = q.pop()
    # print(com,val,c_cnt)
    if com=='n':
        x=(x-1)%(c_cnt//(val+1))+1
    else:
        if c_cnt==x:
            print(val)
            exit()
    # print(x)