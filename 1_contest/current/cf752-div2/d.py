
import sys
input = sys.stdin.readline

def solve():
    x,y=map(int, input().split())
    if x>y:
        print(x+y)
    elif x==y:
        print(x)
    else:
        syo=y//x
        if syo%2==0:
            syo-=1
        val=x*syo
        diff=(y-val)//2
        print(val+diff)


def main():
    # for x in range(2,100,2):
    #     for y in range(x,100,2):
    #         ans=[]
    #         for i in range(1,500):
    #             if i%x==y%i:ans.append(i)
    #         print((x,y),';',ans)
    for _ in range(int(input())):
        solve()
    # solve2(10,68)


if __name__ == "__main__":
    main()