n=int(input())
al=[]
for i in range(60):
    if n==0:
        break
    r=n%3
    if r==0:
        pass
    elif r==1:
        al.append(pow(3,i))
    else:
        al.append(-pow(3,i))
        n+=1
    n//=3
print(len(al))
print(*al)