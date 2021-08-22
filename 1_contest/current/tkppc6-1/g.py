p=int(input())
for pi in range(1,p+1):
    ans=0
    for i in range(pi):
        for j in range(pi):
            for k in range(1,100):
                if pow(i,k,pi)==j:
                    ans+=1
                    break
    print(pi,ans)