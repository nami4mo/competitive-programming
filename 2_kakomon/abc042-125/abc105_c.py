n = int(input())
ans = []
if n == 0:
    print(0)
    exit()
for i in range(10**5):
    if n == 0:
        break
    if n%pow(2,i+1) != 0:
        ans.append('1')
        n -= pow(-2,i)
    else:
        ans.append('0')
    

ans = ans[::-1]
ans_s = ''.join(ans)
print(ans_s)