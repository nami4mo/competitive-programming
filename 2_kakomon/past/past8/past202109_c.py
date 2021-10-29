
def main():
    n,x=map(int, input().split())
    al=list(map(int, input().split()))
    ans=0
    for a in al:
        if a==x:ans+=1
    print(ans)

if __name__ == '__main__':
    main()