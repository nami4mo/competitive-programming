'''
    find minimum x(>=0)
    such that [a*x = b (mod m)]
    by Baby-Step Giant-Step
'''
def calc(a,b,m):
    msqrt=int(m**0.5)+1
    baby={}
    for i in range(msqrt):
        val=(a*i)%m
        baby[val]=i
    for i in range(1,msqrt+1):
        divs_top=(a*i*msqrt-b)%m
        if divs_top in baby:
            back=baby[divs_top]
            ans=((i*msqrt)-back)%m
            return ans
    return -1

ansl=[]
for _ in range(int(input())):
    n,s,k=map(int, input().split())
    ans=calc(k,n-s,n)
    ansl.append(ans)
for a in ansl:print(a)