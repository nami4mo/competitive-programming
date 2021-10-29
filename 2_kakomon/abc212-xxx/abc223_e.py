
def solve(x,y,a,b,c):
    h=(a-1)//x+(b-1)//x+(c-1)//x+3
    if h<=y:
        return True
    
    rem=y-((a-1)//x+1)
    if rem>0:
        w=(b-1)//rem+(c-1)//rem+2
        if w<=x:
            return True

    rem=y-((b-1)//x+1)
    if rem>0:
        w=(c-1)//rem+(a-1)//rem+2
        if w<=x:
            return True
     
    rem=y-((c-1)//x+1)
    if rem>0:
        w=(a-1)//rem+(b-1)//rem+2
        if w<=x:
            return True
         


def main():
    x,y,a,b,c=map(int, input().split())
    if solve(x,y,a,b,c) or solve(y,x,a,b,c):
        print('Yes')
    else:
        print('No')

    

if __name__ == "__main__":
    main()