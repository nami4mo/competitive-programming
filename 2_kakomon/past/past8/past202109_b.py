
def main():
    n,m=map(int, input().split())
    al=list(map(int, input().split()))
    bl=list(map(int, input().split()))
    st=set(bl)
    al.sort()
    ans=[]
    for a in al:
        if a in st:
            ans.append(a)
    print(*ans)

if __name__ == '__main__':
    main()