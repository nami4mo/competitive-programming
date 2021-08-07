def make_ans(s,rs):
    ans=0
    d=rs[0][1]-rs[0][0]
    cnts=[[0]*26 for _ in range((d+1)//2)]
    ones=[0]*26
    oneflag=False
    for l,r in rs:
        for i in range((d+1)//2):
            left=l+i
            right=r-1-i
            if left!=right:
                cl=ord(s[left])-ord('a')
                cr=ord(s[right])-ord('a')
                cnts[i][cl]+=1
                cnts[i][cr]+=1
            else:
                oneflag=True
                cl=ord(s[left])-ord('a')
                ones[cl]+=1

    cs=[]
    mind=10**10
    notcenter=0
    for ri,row in enumerate(cnts[:d//2]):
        csum=0
        cmax=0
        cmax2=0
        maxc=-1
        # print(row)
        for i,v in enumerate(row):
            csum+=v
            if cmax<v:
                cmax,cmax2=v,cmax
                maxc=i
            elif cmax==v:
                cmax,cmax2=v,v
            elif cmax2<v:
                cmax2=v
        ans+=(csum-cmax)
        if (d//2)%2==0 or ri!=(d//2)//2:
            mind=min(cmax-cmax2, mind)
            if (csum-cmax)!=0: notcenter+=1
        cs.append(maxc)

    # print(cs,ans,notcenter)
    csh=cs[:len(cs)]
    if len(csh)>=2 and csh==csh[::-1]:
        if notcenter==0:
            ans+=len(rs)*2
        else:
            ans+=mind


    if oneflag:
        cmax=0
        for c in ones:
            cmax=max(cmax,c)
        ans+=(len(rs)-cmax)

    return ans


k=int(input())
s=list(input())
n=len(s)
rs=[(0,n)]

if k==0:
    if n==1:
        print('impossible')
    elif s==s[::-1]:
        print(1)
    else:
        print(0) 
    exit()      

if n==1:
    if k==1:
        print(0)
    else:
        print('impossible')
    exit()      

one_cnt=0
for _ in range(k-1):
    new_rs=[]
    one_sum=0
    one_cnts=[0]*26
    oneflag=False
    for l,r in rs:
        if r-l==1:
            print('impossible')
            exit()
        if (r-l)%2==0:
            d=(r-l)//2
            new_rs.append((l,l+d))
            new_rs.append((l+d,r))
        else:
            oneflag=True
            d=(r-l)//2
            new_rs.append((l,l+d))
            new_rs.append((l+d+1,r))
            one_cnts[ord(s[l+d])-ord('a')]+=1
            one_sum+=1
    if oneflag:
        cmax=0
        for c in one_cnts:
            cmax=max(cmax,c)
        one_cnt+=(one_sum-cmax)
    # print(rs)
    rs=new_rs[:]

# print(rs)
one_cnt_aaa=0
new_rs=[]
for l,r in rs:
    one_sum=0
    one_cnts=[0]*26
    oneflag=False
    if r-l<=1:
        new_rs=[]
        break
    elif (r-l)%2==0:
        d=(r-l)//2
        new_rs.append((l,l+d))
        new_rs.append((l+d,r))
    else:
        d=(r-l)//2
        new_rs.append((l,l+d))
        new_rs.append((l+d+1,r))
        one_cnts[ord(s[l+d])-ord('a')]+=1
        one_sum+=1
    cmax=0
    for c in one_cnts:
        cmax=max(cmax,c)
    one_cnt_aaa+=(one_sum-cmax)

# print(rs)
d=rs[0][1]-rs[0][0]
if 2<=d<=3:
    print('impossible')
    exit()

ans=make_ans(s,rs)+one_cnt
print(ans)