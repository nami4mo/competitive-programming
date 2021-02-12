n=int(input())
al=list(map(int, input().split()))
atoi={}
for i in range(2**n):
    atoi[al[i]] = i+1

for i in range(n-1):
    new_al=[]
    for i in range(len(al)//2):
        new_al.append(max(al[i*2],al[i*2+1]))
    al=new_al[:]

print(atoi[min(al)])