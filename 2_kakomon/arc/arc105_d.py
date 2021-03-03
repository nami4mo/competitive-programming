import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    if n%2==0:
        d={}
        for a in al:
            d.setdefault(a,0)
            d[a]+=1
        for k,v in d.items():
            if v%2==1:
                print('First')
                break
        else:
            print('Second')
    else:
        print('Second')