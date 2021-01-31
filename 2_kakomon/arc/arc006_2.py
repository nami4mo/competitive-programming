n,l=map(int, input().split())
sl=[]
for _ in range(l):
    row=input().split('|')
    sl.append(row[1:-1])

s=input().rstrip()
s=len(s)//2
# print(s)
# print(sl)
for row in sl[::-1]:
    if s>0 and row[s-1]=='-':
        s-=1
    elif s<n-1 and row[s]=='-':
        s+=1
    
print(s+1)