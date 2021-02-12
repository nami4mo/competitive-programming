class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    n = int(input())
    al = list(map(int, input().split()))
    q = int(input())
    cnt_dic = {}
    ans = 0
    for a in al:
        cnt_dic.setdefault(a,0)
        cnt_dic[a] += 1
        ans += a

    bcl = []
    for _ in range(q):
        b, c = map(int, input().split())
        bcl.append((b,c))


    for bc in bcl:
        b,c = bc
        if b not in cnt_dic:
            print(ans)
            continue
        ans += cnt_dic[b]*(c-b)
        cnt_dic.setdefault(c,0)
        cnt_dic[c] += cnt_dic[b]
        cnt_dic[b] = 0
        print(ans)




if __name__ == "__main__":
    main()