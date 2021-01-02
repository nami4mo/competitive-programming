def to36(num):
    if 0<=num<=9:return str(num)
    return chr(ord('A')+(num-10))

n=int(input())
if n==0:
    print(0)
    exit()
ans=[]
while n>0:
    rem=n%36
    ans.append(to36(rem))
    n//=36
print(''.join(ans[::-1]))