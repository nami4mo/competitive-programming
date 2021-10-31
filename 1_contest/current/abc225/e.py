class Frac:
    def __init__(self, nume, deno):
        self.nume = nume
        self.deno = deno
    def __lt__(self, rh): return self.nume * rh.deno < self.deno * rh.nume
    def __gt__(self, rh): return self.nume * rh.deno > self.deno * rh.nume
    def __eq__(self, rh): return self.nume * rh.deno == self.deno * rh.nume
    def __le__(self, rh): return self.nume * rh.deno <= self.deno * rh.nume
    def __ge__(self, rh): return self.nume * rh.deno >= self.deno * rh.nume
    def __ne__(self, rh): return self.nume * rh.deno != self.deno * rh.nume
    def __repr__(self): return '{}/{}'.format(self.nume, self.deno)

def main():
    n=int(input())
    dl=[]
    for _ in range(n):
        x,y=map(int, input().split())
        dl.append((Frac(y-1,x), Frac(y,x-1)))
    dl.sort(key=lambda x:x[1])
    ans=0
    last=Frac(0,1)
    for d1,d2 in dl:
        if last<=d1:
            ans+=1
            last=d2
    print(ans)


if __name__ == "__main__":
    main()