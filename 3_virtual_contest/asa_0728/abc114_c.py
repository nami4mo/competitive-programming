from itertools import product


def dfs(num_s, n, ansl):
    num = int(num_s)
    if num > n:
        return

    if '7' in num_s and '5' in num_s and '3' in num_s:
        ansl.append(int(num_s))
    dfs(num_s+'7', n, ansl)
    dfs(num_s+'5', n, ansl)
    dfs(num_s+'3', n, ansl)



def main():
    n = int(input())
    ansl = []
    dfs('7',n,ansl)
    dfs('5',n,ansl)
    dfs('3',n,ansl)

    print(len(ansl))


if __name__ == "__main__":
    main()