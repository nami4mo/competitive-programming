def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def main():
    n_ans = [0]*50
    n = int(input())
    if n==1:
        print(0)
        return
        
    facs = factorization(n)

    curr_n = 1
    for i in range(41):
        curr_sum = (curr_n+1)*(curr_n+2)//2
        if i < curr_sum:
            n_ans[i] = curr_n
        else:
            curr_n+=1
            n_ans[i] = curr_n
    # print(n_ans)
            
    ans = 0
    for fac in facs:
        cnt = fac[1]
        ans += n_ans[cnt]
    print(ans)

if __name__ == "__main__":
    main()