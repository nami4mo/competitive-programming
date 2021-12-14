

def main():
    n=int(input())
    nsq = int(n**0.5)
    for i in range(1,10**6+1):
        if i*i>=n:
            nsq=i
            break

    ans=0
    for i in range(1,nsq+1):
        v=n//i
        ans+=v
        # print(i,ans)
    
    for div in range(1,nsq+1):
        left=n//(div+1) +1
        left=max(left,nsq+1)
        right=n//(div)
        # right=max(right)
        cnt=max(0,right-left+1)
        ans+=div*cnt
        # print(div,left,right)

    # for i in range(1,10**6+1):
    #     if i*i==n:
    #         ans-=i


    print(ans)



if __name__ == "__main__":
    main()