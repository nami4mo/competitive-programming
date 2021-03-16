

n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

ans=10**10
for rb in range(2**n):
    # if rb!=3:continue
    colors=[] # 0 or 1
    cl=[]
    c_bit=1
    nums=[]
    for i in range(n):
        if c_bit&rb==0:
            colors.append(0)
            cl.append((al[i],0,i))
            nums.append(al[i])
        else:
            colors.append(1)
            cl.append((bl[i],1,i))
            nums.append(bl[i])
        c_bit*=2

    nums.sort()
    dist=0
    # print(cl)
    for i,num in enumerate(nums):
        # print(cl)
        for j in range(i,n):
            v,col,pos=cl[j]
            if num==v and (pos-i)%2==col:
                dist+=(j-i)
                for k in range(j,i,-1):
                    cl[k],cl[k-1]=cl[k-1],cl[k]
                break
        else:
            # print(i,dist)
            break
    else:
        ans=min(ans,dist)


if ans==10**10:ans=-1
print(ans)
