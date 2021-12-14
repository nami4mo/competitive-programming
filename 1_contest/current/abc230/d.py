

def main():
    n,d=map(int, input().split())
    al=[]
    for _ in range(n):
        l,r=map(int, input().split())
        al.append((l,r))
    al.sort(key=lambda x:x[1])
    ans=1
    right=al[0][1]+d-1
    for l,r in al[1:]:
        if l>right:
            ans+=1
            right=r+d-1
    print(ans)



if __name__ == "__main__":
    main()