from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(ol, gx, gy):
    visited = {}
    q = deque([[0,0]])
    visited[(0,0)] = 0
    while q:
        x, y = q.popleft()
        if [x, y] == [gx, gy]:
            return visited[(gx,gy)]
        for j, k in ([1, 1], [0, 1], [-1, 1], [1, 0], [-1,0], [0,-1]):
            n_x, n_y = x+j, y+k
            if abs(n_x) > 201 or abs(n_y) > 201:
                continue
            if not (n_x,n_y) in ol and not (n_x,n_y) in visited:
                visited[(n_x, n_y)] = visited[(x,y)] + 1
                q.append([n_x,n_y])
    return -1


def main():
    n,x,y = map(int, input().split()) 

    ol = []
    for _ in range(n):
        ox, oy = map(int, input().split()) 
        ol.append( (ox,oy) )
    ol = set(ol)
    ans = bfs(ol, x,y)
    print(ans)


if __name__ == "__main__":
    main()