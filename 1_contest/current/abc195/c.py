n=int(input())

ans=0
for i in range(1,10):
    if n>=pow(10,i*3):
        cnt=pow(10,i*3)-pow(10,(i-1)*3)
        ans+=((i-1)*cnt)
    else:
        cnt=n-pow(10,(i-1)*3)+1
        ans+=((i-1)*cnt)
        break
print(ans)