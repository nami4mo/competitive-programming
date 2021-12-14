
from bisect import bisect_left, bisect_right

def main():
    
    s=input()
    n=len(s)
    k=int(input())
    cnts=[0]
    c=0
    for i in range(n):
        if s[i]=='.':c+=1
        cnts.append(c)
    # print(cnts)
    ans=0
    for i in range(1,n+1):
        k_ok=k+cnts[i-1]
        ind = bisect_right(cnts, k_ok) - 1
        # print(i,ind)
        # ind = ind if 0 <= ind < n else None
        if ind is None: ind=n
        v = ind-i+1
        ans=max(ans,v)
        # print(i,v)
    print(ans)

if __name__ == "__main__":
    main()