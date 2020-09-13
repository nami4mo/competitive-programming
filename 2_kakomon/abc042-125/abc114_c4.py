from collections import deque

def dfs(n):
    stack = deque(['3','5','7'])
    ansl = []
    while stack:
        num_s = stack.pop()
        num = int(num_s)
        if num > n: continue
        if '7' in num_s and '5' in num_s and '3' in num_s:
            ansl.append(num)
        stack.append(num_s+'7')
        stack.append(num_s+'5')
        stack.append(num_s+'3')
    return ansl


def main():
    n = int(input())
    ansl = dfs(n)
    print(len(ansl))


if __name__ == "__main__":
    main()