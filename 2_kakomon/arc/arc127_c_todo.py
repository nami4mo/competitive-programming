def main():
    # a=[
    #     '1',
    #     '10','11',
    #     '100','101','110','111',
    #     '1000','1001','1010','1011','1100','1101','1110','1111'
    # ]
    # a.sort()
    # print(a)
    n=int(input())
    x=input()
    pre='0'*(n-len(x))
    x=pre+x
    x=x[::-1]
    last_one=-1
    for i in range(n):
        if x[i]=='1':
            last_one=i
            break
    ans=[]
    for i in range(n-1,-1,-1):
        


if __name__ == "__main__":
    main()