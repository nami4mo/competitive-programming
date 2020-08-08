from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    yx_p_u = {}
    yx_p_r = {}
    yx_p_d = {}
    yx_p_l = {}

    yx_m_u = {}
    yx_m_r = {}
    yx_m_d = {}
    yx_m_l = {}

    y_d = {}
    y_u = {}
    x_r = {}
    x_l = {}

    for i in range(-200000,200000+1):
        yx_p_u[i] = []
        yx_p_r[i] = []
        yx_p_d[i] = []
        yx_p_l[i] = []

    for i in range(0,400000+1):
        yx_m_u[i] = []
        yx_m_r[i] = []
        yx_m_d[i] = []
        yx_m_l[i] = []

        if i <= 200000:
            y_d[i] = []
            y_u[i] = []
            x_r[i] = []
            x_l[i] = []


    for _ in range(n):
        x,y,u = map(str, input().split())
        x = int(x)
        y = int(y)
        yxp = y-x
        yxm = y+x
        if u == 'U':
            yx_p_u[yxp].append(x)
            yx_m_u[yxm].append(x)
            y_u[x].append(y)
        if u == 'R':
            yx_p_r[yxp].append(x)
            yx_m_r[yxm].append(x)
            x_r[y].append(x)
        if u == 'D':
            yx_p_d[yxp].append(x)
            yx_m_d[yxm].append(x)
            y_d[x].append(y)
        if u == 'L':
            yx_p_l[yxp].append(x)
            yx_m_l[yxm].append(x)
            x_l[y].append(x)


    # for i in range(-20,20+1):
    for i in range(-200000,200000+1):
        yx_p_u[i].sort()
        yx_p_r[i].sort()
        yx_p_d[i].sort()
        yx_p_l[i].sort()

    for i in range(0,400000+1):
        yx_m_u[i].sort()
        yx_m_r[i].sort()
        yx_m_d[i].sort()
        yx_m_l[i].sort()
        if i <= 200000:
            y_d[i].sort()
            y_u[i].sort()
            x_r[i].sort()
            x_l[i].sort()


    ans = 10**9
    for i in range(-200000,200000+1):
        for v in yx_p_u[i]:
            ind = bisect_right(yx_p_l[i], v)
            ind = ind if 0 <= ind < len(yx_p_l[i]) else None
            val = yx_p_l[i][ind] if ind is not None else None
            if val is not None:
                ans = min(ans, abs(val-v)*10)

        for v in yx_p_d[i]:
            ind = bisect_left(yx_p_r[i], v) - 1
            ind = ind if 0 <= ind < len(yx_p_r[i]) else None
            val = yx_p_r[i][ind] if ind is not None else None
            if val is not None:
                ans = min(ans, abs(val-v)*10)


    for i in range(0,400000+1):
        for v in yx_m_d[i]:
            ind = bisect_right(yx_m_l[i], v)
            ind = ind if 0 <= ind < len(yx_m_l[i]) else None
            val = yx_m_l[i][ind] if ind is not None else None
            if val is not None:
                ans = min(ans, abs(val-v)*10)

        for v in yx_m_u[i]:
            ind = bisect_left(yx_m_r[i], v) - 1
            ind = ind if 0 <= ind < len(yx_m_r[i]) else None
            val = yx_m_r[i][ind] if ind is not None else None
            if val is not None:
                ans = min(ans, abs(val-v)*10)

        if i <= 200000:
            for v in y_u[i]:
                ind = bisect_right(y_d[i], v)
                ind = ind if 0 <= ind < len(y_d[i]) else None
                val = y_d[i][ind] if ind is not None else None
                if val is not None:
                    ans = min(ans, abs(val-v)*10//2)

            for v in x_r[i]:
                ind = bisect_right(x_l[i], v)
                ind = ind if 0 <= ind < len(x_l[i]) else None
                val = x_l[i][ind] if ind is not None else None
                if val is not None:
                    ans = min(ans, abs(val-v)*10//2)


    if ans == 10**9:
        print('SAFE')
    else:
        print(ans)


if __name__ == "__main__":
    main()