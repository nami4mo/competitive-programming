

def main():
    n2,n3,n4=map(int, input().split())
    ans=0

    c3=n3//2
    c4=n4
    cnt=min(c3,c4)
    ans+=cnt
    n3-=cnt*2
    n4-=cnt*1

    c3=n3//2
    c2=n2//2
    cnt=min(c3,c2)
    ans+=cnt
    n3-=cnt*2
    n2-=cnt*2
    
    c4=n4//2
    c2=n2//1
    cnt=min(c4,c2)
    ans+=cnt
    n4-=cnt*2
    n2-=cnt*1


    if n4==1:
        n2+=n4*2
    ans+=n2//5
    print(ans)



if __name__ == "__main__":
    for _ in range(int(input())):
        main()
