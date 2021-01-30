
def solve(l,r):
    MOD=10**9+7
    ans=0

    lbit=[]
    rbit=[]
    cl,cr=l,r
    for bit in range(60):
        lbit.append(cl&1)
        rbit.append(cr&1)
        cl>>=1
        cr>>=1


    for bit in range(60):
        bit2=pow(2,bit)
        bit21=pow(2,bit+1)
        if bit2>r: break
        if l>bit21-1:continue

        if r>=bit21 and l<=bit2:
            ans+=pow(3,bit,MOD)
        
        elif r>=bit21 and l>bit2:
            dp_same=[0]*(bit+1)
            dp_large=[0]*(bit+1)
            dp_same[0]=1
            for i in range(bit):
                bit_i=bit-1-i
                if lbit[bit_i]==1:
                    dp_same[i+1]=dp_same[i]
                    dp_large[i+1]=dp_large[i]*3
                else:
                    dp_same[i+1]=dp_same[i]*2
                    dp_large[i+1]=dp_large[i]*3+dp_same[i]
            ans+=dp_same[-1]
            ans+=dp_large[-1]
            ans%=MOD
        
        elif r<bit21 and l<=bit2:
            dp_same=[0]*(bit+1)
            dp_small=[0]*(bit+1)
            dp_same[0]=1
            for i in range(bit):
                bit_i=bit-1-i
                if rbit[bit_i]==1:
                    dp_same[i+1]=dp_same[i]*2
                    dp_small[i+1]=dp_small[i]*3+dp_same[i]
                else:
                    dp_same[i+1]=dp_same[i]
                    dp_small[i+1]=dp_small[i]*3
            ans+=dp_same[-1]
            ans+=dp_small[-1]
            ans%=MOD

        else:
            dp_same_same=[0]*(bit+1)
            dp_same_small=[0]*(bit+1)
            dp_large_same=[0]*(bit+1)
            dp_large_small=[0]*(bit+1)
            dp_same_same[0]=1
            for i in range(bit):
                bit_i=bit-1-i
                li,ri=lbit[bit_i],rbit[bit_i]

                if li==0 and ri==0:
                    dp_same_same[i+1]=dp_same_same[i]
                    dp_same_small[i+1]=dp_same_small[i]*2
                    dp_large_same[i+1]=dp_large_same[i]
                    dp_large_small[i+1]=dp_large_small[i]*3+dp_same_small[i]

                elif li==0 and ri==1:
                    dp_same_same[i+1]=dp_same_same[i]
                    dp_same_small[i+1]=dp_same_small[i]*2+dp_same_same[i]
                    dp_large_same[i+1]=dp_large_same[i]*2+dp_same_same[i]
                    dp_large_small[i+1]=dp_large_small[i]*3+dp_same_small[i]+dp_large_same[i]

                elif li==1 and ri==0:
                    # dp_same_same[i+1]=dp_same_same[i]
                    dp_same_same[i+1]=0
                    dp_same_small[i+1]=dp_same_small[i]
                    dp_large_same[i+1]=dp_large_same[i]
                    dp_large_small[i+1]=dp_large_small[i]*3

                elif li==1 and ri==1:
                    dp_same_same[i+1]=dp_same_same[i]
                    dp_same_small[i+1]=dp_same_small[i]
                    dp_large_same[i+1]=dp_large_same[i]*2
                    dp_large_small[i+1]=dp_large_small[i]*3+dp_large_same[i]

                ans+=dp_same_same[-1]
                ans+=dp_same_small[-1]
                ans+=dp_large_same[-1]
                ans+=dp_large_small[-1]
                ans%=MOD
        # print(bit,ans)
    return ans

def solve2(l,r):
    ans=0
    for x in range(l,r+1):
        for y in range(x,r+1):
            if x^y==y%x:ans+=1
    return ans



l,r=map(int, input().split())
ans=solve(l,r)
print(ans)

# for i in range(1,10):
#     for j in range(i+1,10):
#         print(i,j,solve(i,j), solve2(i,j))