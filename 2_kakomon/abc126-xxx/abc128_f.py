n=int(input())
al=list(map(int, input().split()))

ans=0
for step in range(1,n):
    fronts=[]
    csum=0
    pos=0
    while pos<=n-1:
        csum+=al[pos]
        fronts.append(csum)
        pos+=step
    bsum=0
    st=set()
    for j in range(n):
        pos = n-1-step*(j+1)
        if pos<=step:break
        st.add(pos)
        if pos%step==0 and pos<=j*step:break
        fronts_ind=(j+1)*step
        if fronts_ind in st:break
        bsum+=al[pos]
        val = fronts[j+1]+bsum
        ans=max(ans,val)
        # if ans==val:
        #     print('---',step,j,val)
            

print(ans)
