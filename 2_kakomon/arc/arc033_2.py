na,nb=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
st1=set(al+bl)
ast,bst=set(al),set(bl)
st2=ast&bst
ans=len(st2)/len(st1)
print(ans)