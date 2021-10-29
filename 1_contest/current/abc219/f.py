
def main():
    st=set()
    y,x=0,0
    st.add((0,0))
    s=input()
    k=int(input())
    prev_update=0
    prev=0
    rem=0
    for ki in range(k):
        for si in s:
            if si=='L':x-=1
            if si=='R':x+=1
            if si=='U':y+=1
            if si=='D':y-=1
            st.add((y,x))
        cnt=len(st)
        update=cnt-prev
        prev=cnt
        if update==prev_update:
            rem=k-ki-1
            break
        prev_update=update

    ans=len(st)+prev_update*rem
    print(ans)



if __name__ == "__main__":
    main()