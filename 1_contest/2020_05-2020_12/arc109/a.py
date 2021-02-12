a,b,x,y = map(int, input().split())

if a > b:
    diff = a-b-1
    ans1 = diff*y + x
    ans2 = ((a-b)*2-1)*x
    print(min(ans1,ans2))

elif a == b:
    print(x)

else:
    ans1 = ((b-a)*2+1)*x
    ans2 = (b-a)*y+x
    print(min(ans1,ans2))