k=int(input())

# com2=[]
# for i in range()

# ans=0
# cnt=0
c1=0
c2=0
c3=0
for a in range(1,k+1):
    for b in range(a,k+1):
        if a*b>k:break
        c=k//(a*b)
        if c<b:break
        # ans+=c
        if a==b:
            if c>=b:
                c3+=1
                c2+=(c-b)
            else:
                c2+=c
        else:
            c2+=1
            c1+=(c-b)

ans=c1*6+c2*3+c3
print(ans)

# print(cnt)