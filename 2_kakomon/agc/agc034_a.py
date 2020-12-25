n,a,b,c,d=map(int, input().split())
a-=1
b-=1
c-=1
d-=1
# s=list(input())
s=input()

def fail():
    print('No')
    exit()

if c<d:
    if '##' in s[b:d+1]:
        fail()
    if '##' in s[a:c+1]:
        fail()
    print('Yes')
    exit()

if not '...' in s[b-1:d+2]:
    fail()
if '##' in s[b:d+1]:
    fail()
if '##' in s[a:c+1]:
    fail()
print('Yes')