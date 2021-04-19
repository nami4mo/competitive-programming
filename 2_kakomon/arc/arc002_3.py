n=int(input())
s=input()
s=s.replace('A','0').replace('B','1').replace('X','2').replace('Y','3')

ans=10**10
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ss=s.replace(str(i)+str(j),'x').replace(str(k)+str(l),'y')
                ans=min(ans,len(ss))
print(ans)