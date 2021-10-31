

def main():
    n,q=map(int, input().split())
    front=[-1]*(n+1)
    back=[-1]*(n+1)
    for _ in range(q):
        ql=list(map(int, input().split()))
        if ql[0]==1:
            a,b=ql[1],ql[2]
            back[a]=b
            front[b]=a
        elif ql[0]==2:
            a,b=ql[1],ql[2]
            back[a]=-1
            front[b]=-1
        else:
            x=ql[1]
            fs=[]
            curr=front[x]
            while curr!=-1:
                fs.append(curr)
                curr=front[curr]
            fs=fs[::-1]

            fs.append(x)

            curr=back[x]
            while curr!=-1:
                fs.append(curr)
                curr=back[curr]

            print(len(fs), *fs)
        # print('---', front, back)

if __name__ == "__main__":
    main()